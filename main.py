from Euler import euler as method
from Euler import NAME_ERROR
from RK4 import rk4

import numpy as np
import matplotlib.pyplot as plt

T = 15


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

    # Зависимости переменных от времени
    u0 = u0_list[0]
    t, u = method(f, u0, 0.0, T, 1e-3)

    fig_t, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
    labels = ['x(t)', 'y(t)', 'z(t)']
    colors_t = ['darkred', 'navy', 'darkgreen']

    for i, ax_i in enumerate(axes):
        ax_i.plot(t, u[:, i], color=colors_t[i], lw=0.8)
        ax_i.set_ylabel(labels[i])
        ax_i.grid(True, which='both', ls=':')

    axes[-1].set_xlabel('t')
    fig_t.suptitle(f'Зависимости от времени, u0={tuple(u0)}')
    plt.tight_layout()
    plt.show()

    # Ошибка и порядок

    hs = np.array([0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001])
    if method != rk4:
        u_exact = rk4(f, u0, 0.0, T, 1e-5)[1][-1]

        errs = np.array([np.linalg.norm(method(f, u0, 0.0, T, h)[1][-1] - u_exact, np.inf)
                         for h in hs])
    else:
        U_h = [rk4(f, u0, 0.0, T, h)[1][-1] for h in hs]
        U_h2 = [rk4(f, u0, 0.0, T, h / 2)[1][-1] for h in hs]
        errs = np.array([np.linalg.norm(a - b, np.inf) for a, b in zip(U_h, U_h2)])

    p_fit = np.polyfit(np.log(hs), np.log(errs), 1)[0]

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
