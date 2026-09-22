import numpy as np

NAME_ERROR = "Ошибка RK4 ‖u_h − u_{h/2}‖"


def rk4(f, u0, t0, t1, h):
    n = int(round((t1 - t0) / h))
    t = t0 + h * np.arange(n + 1)

    u = np.zeros((n + 1, 3))
    u[0] = u0

    for i in range(n):
        k1 = f(u[i])
        k2 = f(u[i] + 0.5 * h * k1)
        k3 = f(u[i] + 0.5 * h * k2)
        k4 = f(u[i] + h * k3)
        u[i + 1] = u[i] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return t, u