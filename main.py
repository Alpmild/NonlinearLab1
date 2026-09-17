from EMP import emp as method
from EMP import NAME_ERROR
from RK4 import rk4

import numpy as np
import matplotlib.pyplot as plt

T = 5


def f(u):
    x, y, z = u
    return np.array([y * z, x - y, 1 - x * y])


if __name__ == '__main__':

    # Фазовый портрет
    u0_list = [(1, 0.5, 0), (-2, 1, 1), (0, -1.5, 2), (2, 2, -1), (-1, -1, -1)]
    colors = ['darkred', 'navy', 'darkgreen', 'darkorange', 'purple']

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    for u0, c in zip(u0_list, colors):
        _, u = method(f, u0, 0.0, 40.0, 1e-3)

        ax.plot(u[:, 0], u[:, 1], u[:, 2], lw=0.6, color=c, label=f'u0={u0}')
        ax.scatter(*u0, color=c, s=30)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.legend(fontsize=8)
    plt.show()

    # Ошибка и порядок
    u0 = np.array([1, 1, 1])
    u_exact = rk4(f, u0, 0.0, T, 1e-5)[1][-1]

    hs = np.array([0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001])
    errs = np.array([np.linalg.norm(method(f, u0, 0.0, T, h)[1][-1] - u_exact, np.inf)
                     for h in hs])

    p_fit = np.polyfit(np.log(hs), np.log(errs), 1)[0]  # порядок по МНК

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.loglog(hs, errs, 'o-', color='darkred', label=NAME_ERROR)
    ax.loglog(hs, errs[0] * (hs / hs[0]) ** p_fit, '--', color='gray',
              label=f'Наклон p = {p_fit:.3f}')

    ax.set_xlabel('Шаг h')
    ax.set_ylabel('Глобальная ошибка')
    ax.grid(True, which='both', ls=':')
    ax.legend()
    plt.show()

    print(f"Порядок метода: {p_fit:.3f}")
