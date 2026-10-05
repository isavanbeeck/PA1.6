from typing import Optional
from utils.rng import RNG

def step_room(T: float, heater_on: int, T_out: float, R: float, C: float, P: float,
              dt: float, process_sigma: float = 0.0, rng: Optional[RNG] = None) -> float:
    ''' Simulate one time step of a simple RC room thermal model.
        T: Current room temperature (degrees Celsius).
        heater_on: Heater state (0=OFF, 1=ON).
        T_out: Outside temperature (degrees Celsius).
        R: Thermal resistance (degrees Celsius per Watt).
        C: Thermal capacitance (Joules per degrees Celsius).
        P: Heater power when ON (Watts).
        dt: Time step duration (seconds).
        process_sigma: Standard deviation of process noise (degrees Celsius).
        rng: Optional random number generator for noise.
        Returns the updated room temperature after time step dt.
    '''
    # --- Student code starts here ---
    # Hint: Use the Euler method to integrate the differential equation.
    # RC model: dT/dt = (T_out - T)/(R*C) + heater_on * P/C + noise
    
    # --- Student code ends here ---
    return 0.0 # remove when code is added
