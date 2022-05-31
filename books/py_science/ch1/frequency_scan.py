import numpy as np
from scipy import signal
import pylab as pl


if __name__ == "__main__":
    t = np.linspace(0, 10, 1000)
    x = signal.chirp(t, 5, 10, 30)
    print(x[:50])
    pl.plot(t, x)
    pl.gca().lines[0].set_color("r")
    pl.show()
