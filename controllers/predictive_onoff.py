from dataclasses import dataclass

@dataclass
class PredictiveOnOff:
    setpoint: float
    deadband: float
    tau: float = 10.0         # lookahead horizon (seconds)
    safety_high: float = 26.0
    state: int = 0            # 0=OFF, 1=ON

    # Exposed diagnostics for plotting/logging
    last_meas: float | None = None
    last_pred: float | None = None
    lower_threshold: float | None = None
    upper_threshold: float | None = None

    def update(self, meas_filtered: float, dt: float) -> int:
        ''' Update the thermostat state based on the measured temperature and a prediction.
            If the predicted temperature (based on current trend) is below the lower threshold
            (setpoint - deadband/2), the thermostat turns ON (state=1).
            If the predicted temperature is above the upper threshold (setpoint + deadband/2),
            the thermostat turns OFF (state=0).
            If the measured temperature exceeds the safety_high limit, the thermostat turns OFF.
            meas_filtered: The current filtered/measured temperature.
            dt: Time difference since last update (seconds).
            Returns the current state (0=OFF, 1=ON).
        '''

        if meas_filtered >= self.safety_high:
            self.state = 0
            self._update_diag(meas_filtered, dt, meas_filtered)  # pred doesn't matter here
            return self.state

        # Predict a short time into the future using discrete derivative
        if self.last_meas is None:
            T_pred = meas_filtered
        else:
            dTdt = (meas_filtered - self.last_meas) / dt
            T_pred = meas_filtered + self.tau * dTdt

        lower = self.setpoint - self.deadband / 2.0
        upper = self.setpoint + self.deadband / 2.0

        # Decision using predicted temperature
        if T_pred < lower:
            self.state = 1
        elif T_pred > upper:
            self.state = 0
        # else: keep previous state

        self._update_diag(meas_filtered, dt, T_pred, lower, upper)
        return self.state

    def _update_diag(self, meas: float, dt: float, T_pred: float, lower: float | None = None, upper: float | None = None):
        ''' Update diagnostic variables for logging/plotting. 
            This includes the last measured temperature, the last predicted temperature,
            and the current lower and upper thresholds based on setpoint and deadband.
        '''
        self.last_pred = T_pred
        self.last_meas = meas
        if lower is None or upper is None:
            lower = self.setpoint - self.deadband / 2.0
            upper = self.setpoint + self.deadband / 2.0
        self.lower_threshold = lower
        self.upper_threshold = upper
