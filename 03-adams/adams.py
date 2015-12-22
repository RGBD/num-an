#!/usr/bin/python3
import math
import pdb

VERBOSE = False

def rk4(f, t_0, x_0, h, n):
    x = [x_0]
    t = t_0
    for i in range(n):
        k_1 = f(t, x[-1])
        k_2 = f(t + 0.5 * h, x[-1] + k_1 * 0.5 * h)
        k_3 = f(t + 0.5 * h, x[-1] + k_2 * 0.5 * h)
        k_4 = f(t + h, x[-1] + k_3 * h)
        x_new = x[-1] + h / 6.0 * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        x.append(x_new)
        t += h
    return x

def adams2_extra(f, t, x, h):
    n = len(x) - 1
    return x[n] + h / 12.0 * (23 * f[n] - 16 * f[n - 1] + 5 * f[n - 2])

def adams2_inter(f, t, x, h):
    n = len(x) - 1
    return x[n] + h / 24.0 * (9 * f[n + 1] + 19 * f[n]
                              - 5 * f[n - 1] + f[n - 2])

"""
Runge Kutta 4 at the beginning,
Adams (q = 2) extrapolation as a predictor,
Adams (q = 2) interpolation as a corrector.
"""
def method(f, t_0, x_0, h, n):
    PARAM_Q = 2

    f_function = f
    x = rk4(f, t_0, x_0, h, PARAM_Q)
    if VERBOSE:
        for i in range(PARAM_Q + 1):
            print("-" * 30)
            print("n = %d" % i)
            print("t = %f" % (t_0 + i * h))
            print("x =", x[i])
        input("")

    if (n <= len(x)):
        return x[:PARAM_Q + 1]

    f = [f_function(t_0 + i * h, x) for i, x in enumerate(x)]
    t = t_0 + (PARAM_Q + 1) * h
    for n in range(PARAM_Q, n):
        x_pred = adams2_extra(f, t, x, h)
        f.append(f_function(t, x_pred))
        x_corr = adams2_inter(f, t, x, h)
        x.append(x_corr)
        f[-1] = f_function(t, x_corr)
        if VERBOSE:
            print("-" * 30)
            print("n = %d" % n)
            print("t = %f" % t)
            print("f =", f[-1])
            print("p =", x[-1])
            print("c =", x[-1])
            input("")
        t += h
    return x
