#!/usr/bin/python3
import math
from adams import method, rk4

x = lambda t: 2 * math.pow(math.e, -t) + t - 1
f = lambda t, x: -float(x) + t

t_0 = 0.0
x_0 = 1.0

h = 0.1
n = 10

print("method")
print("v" * 30 + "\n\n")
x_method = method(f, t_0, x_0, h, n)
print(x_method)
print("-" * 30 + "\n\n")

print("v" * 30 + "\n\n")
x_precise = [x(t_0 + i * h) for i in range(n + 1)]
print(x_precise)
print("-" * 30 + "\n\n")

err_precise = math.fabs(x_precise[-1] - x_method[-1])

print("=" * 30)
print("x_method    = %.15f" % x_method[-1])
print("x_precise   = %.15f" % x_precise[-1])
print("err_precise = %.15f" % err_precise)

for i, x in enumerate(x_method):
    print("x_{%d} &= %f\\\\" % (i, x))
