import numpy as np

NAME_ERROR = 'Ошибка Эйлера-Крамера'


def euler_kromer(f, u0, t0, t1, h):
    n = int(round((t1 - t0) / h))
    t = t0 + h * np.arange(n + 1)

    u = np.zeros((n + 1, 3))
    u[0] = u0

    for i in range(n):
        x, y, z = u[i]

        x_new = x + h * y * z
        y_new = y + h * (x_new - y)
        z_new = z + h * (1 - x_new * y_new)

        u[i + 1] = [x_new, y_new, z_new]

    return t, u
