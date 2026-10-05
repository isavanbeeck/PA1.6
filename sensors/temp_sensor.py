from dataclasses import dataclass
from typing import Optional
from utils.rng import RNG

@dataclass
class TempSensor:
    sigma: float = 0.2
    bias: float = 0.3
    dropout_prob: float = 0.02
    rng: Optional[RNG] = None

    def read(self, true_temp: float) -> Optional[float]:
        ''' Simulate a temperature sensor reading with Gaussian noise, bias, and dropout.
            true_temp: The actual temperature to be measured.
            Returns the noisy temperature reading, or None if the sensor drops out.
        '''
        if self.rng is None:
            raise ValueError("TempSensor requires a RNG")
        if self.rng.bernoulli(self.dropout_prob):
            return None
        noisy = true_temp + self.bias + self.rng.gauss(0.0, self.sigma)
        return noisy
