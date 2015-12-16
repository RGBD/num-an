#!/usr/bin/python3
import math
from rk4 import rk4

x = lambda t: 2 * math.pow(math.e, -t) + t - 1
f = lambda t, x: -float(x) + t

t_0 = 0.0
x_0 = 1.0

eps = 1e-4

h = 0.1
n = 10

print("runge-kutta with h")
print("v" * 30 + "\n\n")
x_h = rk4(f, t_0, x_0, h, n)
print("-" * 30 + "\n\n")

print("runge-kutta with h/2")
print("v" * 30 + "\n\n")
x_h2 = rk4(f, t_0, x_0, 0.5 * h, 2 * n)
print("-" * 30 + "\n\n")

x_precise = x(t_0 + h * n)

err_runge = math.fabs(x_h[-1] - x_h2[-1])
err_precise = math.fabs(x_precise - x_h2[-1])

print("=" * 30)
print("x_h         = %.15f" % x_h[-1])
print("x_[h/2]     = %.15f" % x_h2[-1])
print("x_precise   = %.15f" % x_precise)
print("err_runge   = %.15f" % err_runge)
print("err_precise = %.15f" % err_precise)

if  err_runge < eps * (2**4 - 1):
    print("precision reached")
else:
    print("precision not reached, need smaller step")

errors = [math.fabs(a - b) for a, b in zip(x_h, x_h2[::2])]

for i, e in enumerate(errors):
    print("|x_{%2d, h} - x_{%2d, h/2}| = %.15f\\" % (i, i, e))
