#!/usr/bin/python3
import math
from pred_corr import pred_corr

x = lambda t: 2 * math.pow(math.e, -t) + t - 1
f = lambda t, x: -x + t

t_0 = 0.0
x_0 = 1.0

eps = 1e-4

h = 0.1
n = 10

print("pred_corr(h)")
print("v" * 30 + "\n\n")
x_n, h_n, eps_n = pred_corr(f, t_0, x_0, h, n, eps)
print("-" * 30 + "\n\n")

x_precise = x(t_0 + h * n)

err_method = math.fabs(max([math.fabs(x) for x in eps_n]))
err_precise = math.fabs(x_precise - x_n[-1])

print("=" * 30)
print("x_n         = %.15f" % x_n[-1])
print("x_precise   = %.15f" % x_precise)
print("err_method  = %.15f" % err_method)
print("err_precise = %.15f" % err_precise)

if  err_method < eps:
    print("precision reached")
else:
    print("precision not reached, need smaller step")

errors = eps_n

for i, e in enumerate(errors):
    print("|x_{%2d}^{[4]} - x_{%2d}^{[3]}| = %.15f\\\\" % (i, i, e))
