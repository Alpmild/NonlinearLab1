import numpy as np

NAME_ERROR = 'Ошибка EMP'


def emp(f, u0, t0, t1, h):
    n = int(round((t1 - t0) / h))
    t = t0 + h * np.arange(n + 1)

    u = np.zeros((n + 1, 3))
    u[0] = u0

    h1 = h / 2

    for i in range(n):
        mid = u[i] + h1 * f(u[i])
        u[i + 1] = u[i] + h * f(mid)

    return t, u
