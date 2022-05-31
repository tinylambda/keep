import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    data = np.genfromtxt("co2.csv", delimiter=",")
    plt.plot(data[:, 0], data[:, 1])
    plt.xlabel("$year$", fontsize=16)
    plt.ylabel("$CO_2 (ppmv)$", fontsize=16)
    plt.show()
