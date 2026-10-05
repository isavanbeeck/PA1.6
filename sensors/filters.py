from typing import Optional

def hold_last(value: Optional[float], last: Optional[float]) -> Optional[float]:
    return last if value is None else value

class MovingAverageFilter:
    def __init__(self, window: int = 5):
        assert window >= 1
        self.window = window
        self.buf = []
        self.sum = 0.0

    def update(self, x: float) -> float:
        ''' Update the moving average filter with a new value x.
            Returns the current filtered value.
        '''
        self.buf.append(x)
        self.sum += x
        if len(self.buf) > self.window:
            self.sum -= self.buf.pop(0)
        return self.sum / len(self.buf)
