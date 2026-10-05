from dataclasses import dataclass

@dataclass
class OnOffThermostat:
    setpoint: float
    deadband: float
    safety_high: float = 26.0
    state: int = 0  # 0=OFF, 1=ON

    def update(self, measured_temp: float) -> int:
        ''' Update the thermostat state based on the measured temperature.
            If the measured temperature is below the lower threshold (setpoint - deadband/2),
            the thermostat turns ON (state=1).
            If the measured temperature is above the upper threshold (setpoint + deadband/2),
            the thermostat turns OFF (state=0).
            If the measured temperature exceeds the safety_high limit, the thermostat turns OFF.
            Returns the current state (0=OFF, 1=ON).
        '''
        #lower = self.setpoint ... self.deadband ...
        #upper = self.setpoint ... self.deadband ...
        #if self.safety_high ... :
        #    self.state ...
        #    return self.state
        #if ...:
        #    self.state ...
        #elif ...:
        return self.state
