#!/usr/bin/python3
import math
from fin_diff import fin_diff

phi = lambda x: x ** 2 + 1.0
phi_xx = lambda x: 2.0
psi = lambda x: x + 1.0
mu_0 = lambda t: t + 1.0
mu_1 = lambda t: t + 2.0
f = lambda x, t: x * math.e ** t

x_0 = 0.0
x_1 = 1.0
t_0 = 0.0
t_1 = 1.0

x_count = 100
t_count = 100

y = fin_diff(phi, phi_xx, psi, mu_0, mu_1, f,
             x_0, x_1, t_0, t_1,
             x_count, t_count)

print("{\n" + ",\n".join(["%.4f" % y for y in y])+ "\n}")
