from numpy.random import default_rng

class RNG:
    def __init__(self, seed: int):
        self.rng = default_rng(seed)

    def gauss(self, mu: float, sigma: float) -> float:
        ''' Return a random float following a Gaussian distribution with mean mu and standard deviation sigma. '''
        return float(self.rng.normal(mu, sigma))

    def uniform(self, a: float, b: float) -> float:
        ''' Return a random float in the range [a, b) following a uniform distribution. '''
        return float(self.rng.uniform(a, b))

    def bernoulli(self, p: float) -> bool:
        ''' Return True with probability p, False with probability 1-p. '''
        return bool(self.rng.random() < p)
