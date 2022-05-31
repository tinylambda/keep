import math
from collections import Sequence


def s0(samples: Sequence) -> float:
    return sum(1 for x in samples)


def s1(samples: Sequence) -> float:
    return sum(x for x in samples)


def s2(samples: Sequence) -> float:
    return sum(x**2 for x in samples)


def mean(samples: Sequence) -> float:
    return s1(samples) / s0(samples)


def stdev(samples: Sequence) -> float:
    N = s0(samples)
    return math.sqrt(s2(samples) / N - (s1(samples) / N) ** 2)


def z(x, mu_x: float, rou_x: float) -> float:
    return (x - mu_x) / rou_x


def corr(samples1: Sequence, samples2: Sequence) -> float:
    m_1, s_1 = mean(samples1), stdev(samples1)
    m_2, s_2 = mean(samples2), stdev(samples2)

    z_1 = (z(x, m_1, s_1) for x in samples1)
    z_2 = (z(x, m_2, s_2) for x in samples2)

    r = (sum(zx1 * zx2 for zx1, zx2 in zip(z_1, z_2))) / len(samples1)
    return r


if __name__ == "__main__":
    d = [2, 4, 4, 4, 5, 5, 7, 9]
    print(list(z(x, mean(d), stdev(d)) for x in d))

    xi = [
        1.47,
        1.50,
        1.52,
        1.55,
        1.57,
        1.60,
        1.63,
        1.65,
        1.68,
        1.70,
        1.73,
        1.75,
        1.78,
        1.80,
        1.83,
    ]
    yi = [
        52.21,
        53.12,
        54.48,
        55.84,
        57.20,
        58.57,
        59.93,
        61.29,
        63.11,
        64.47,
        66.28,
        68.10,
        69.92,
        72.19,
        74.46,
    ]
    print(len(xi), len(yi), round(corr(xi, yi), 5))
