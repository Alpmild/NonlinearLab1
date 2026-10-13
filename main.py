import os
import numpy as np
import matplotlib.pyplot as plt

from Euler import euler
from EulerKromer import euler_kromer
from EMP import emp
from KD import kd
from RK4 import rk4

h = 0.0001

u = [0.1, 0.1, 0.1]

start_params = [1, 1, 1]

N = 1_000_000
transient = 1

a1_values = np.linspace(-0.2, 1.5, 1000)
a2_values = np.linspace(-0.1, 3.0, 1000)
a3_values = np.linspace(-0.2, 1.5, 1000)

save_folder = "bifurcation_plots"
os.makedirs(save_folder, exist_ok=True)

methods = [
    ("Euler", euler),
    ("Euler-Cromer", euler_kromer),
    ("EMP", emp),
    ("VSKD", kd),
]

parameters = [
    ("a1", a1_values),
    ("a2", a2_values),
    ("a3", a3_values),
]


def f(u, a1, a2, a3):
    x, y, z = u
    return np.array([a1 * y * z, x - a2 * y, a3 - x * y])


def bifurcation(method, method_name, parameter, parameter_name, u, start_params, params:
    pass

save_folder = 'bifurcation_plots'
os.makedirs(save_folder, exist_ok=True)


for i in range(len(methods)):
    method_name, method = methods[i]
    for j in range(len(parameters)):
        parameter_name, params = parameters[i]




# # ---------- параметры ----------
# h = 1e-4
# u0 = np.array([0.1, 0.1, 0.1])
# a0 = {'a1': 1.0, 'a2': 1.0, 'a3': 1.0}
# N = 1_000_000           # для проверки можно взять 100_000
# t0, t1 = 0.0, N * h
# transient = 0.7
#
# sweeps = {
#     'a1': np.linspace(-0.2, 1.5, 20),
#     'a2': np.linspace(-0.1, 3.0, 20),
#     'a3': np.linspace(-0.2, 1.5, 20),
# }
#
# save_folder = 'bifurcation_plots'
# os.makedirs(save_folder, exist_ok=True)
#
# # ---------- система ----------
# def make_f(a1, a2, a3):
#     def f(u):
#         x, y, z = u
#         return np.array([a1 * y * z, x - a2 * y, a3 - x * x])
#     return f
#
# # единый интерфейс: method(f, u0, t0, t1, h, p)
# methods = {
#     'Euler':        euler,
#     'Euler-Cromer': euler_cramer,
#     'EMP':          emp,
#     'VSKD':         kd,
# }
# rk4_method = rk4
#
# # ---------- вспомогательные ----------
# def simulate(method, p):
#     """Возвращает x(t) или None, если траектория разошлась."""
#     f = make_f(*p)
#     with np.errstate(all='ignore'):
#         try:
#             _, u = method(f, u0, t0, t1, h, p)
#         except Exception:
#             return None
#         if not np.all(np.isfinite(u)) or np.max(np.abs(u)) > 1e6:
#             return None
#     return u[:, 0]
#
# def find_maxima(x, transient):
#     x = x[int(round(len(x) * transient)):]
#     if len(x) < 3:
#         return np.array([])
#     mid = x[1:-1]
#     idx = np.where((mid > x[:-2]) & (mid > x[2:]))[0] + 1
#     return x[idx]
#
# # ---------- основной цикл ----------
# for param_name, values in sweeps.items():
#
#     # RK4 считаем один раз на каждое значение параметра
#     rk4_p, rk4_x = [], []
#     method_data = {name: ([], []) for name in methods}
#
#     for k, value in enumerate(values):
#         print(f'\r{param_name}: {k + 1}/{len(values)}', end='')
#
#         a = dict(a0)
#         a[param_name] = value
#         p = (a['a1'], a['a2'], a['a3'])
#
#         x_rk = simulate(rk4_method, p)
#         if x_rk is not None:
#             m = find_maxima(x_rk, transient)
#             rk4_p.append(np.full(len(m), value))
#             rk4_x.append(m)
#
#         for name, method in methods.items():
#             x_m = simulate(method, p)
#             if x_m is not None:
#                 m = find_maxima(x_m, transient)
#                 method_data[name][0].append(np.full(len(m), value))
#                 method_data[name][1].append(m)
#     print()
#
#     cat = lambda lst: np.concatenate(lst) if lst else np.array([])
#     rp, rx = cat(rk4_p), cat(rk4_x)
#
#     for name in methods:
#         mp, mx = cat(method_data[name][0]), cat(method_data[name][1])
#
#         plt.figure(figsize=(8, 5))
#         if mx.size:
#             plt.scatter(mp, mx, s=5, c='b', alpha=0.8, label=name, linewidths=0)
#         if rx.size:
#             plt.scatter(rp, rx, s=5, c='r', alpha=0.4, label='RK4', linewidths=0)
#
#         plt.xlabel(param_name)
#         plt.ylabel('Экстремумы x')
#         plt.title(f'Sprott Case C: {param_name}, {name} и RK4')
#         plt.legend(loc='best')
#         plt.grid(True)
#         plt.xlim(values.min(), values.max())
#         plt.ylim(-2, 4)
#
#         path = os.path.join(save_folder, f'Case_C_{param_name}_{name}.png')
#         plt.savefig(path, dpi=150)
#         plt.close()
#         print('График сохранен:', path)
