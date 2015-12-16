#!/usr/bin/python3
import math

def rk4(f, t_0, x_0, h, n):
    print("t_0 = %.15f" % t_0)
    print("x_0 = %.15f" % x_0)
    print("h   = %.15f" % h)
    print("n   = %d" % n)

    x = [x_0]
    t = t_0

    for i in range(n):
        k_1 = f(t, x[-1])
        k_2 = f(t + 0.5 * h, x[-1] + k_1 * 0.5 * h)
        k_3 = f(t + 0.5 * h, x[-1] + k_2 * 0.5 * h)
        k_4 = f(t + h, x[-1] + k_3 * h)
        x_new = x[-1] + h / 6.0 * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        x_composed = x[-1] * (1 + h + 1/2*h**2 + 1/6*h**3 + 1/24*h**4)\
                   + 1 * (1/2*h**2 + 1/6*h**3 + 1/24*h**4)\
                   + t * (h + 1/2*h**2 + 1/6*h**3 + 1/24*h**4)

        print("x_new - x_composed = %lf - %lf = %lf"
              % (x_new, x_composed, x_new - x_composed))

        print("-" * 30)
        print("step %d" % (i + 1))
        print("x   = %.15f" % x[-1])
        print("k_1 = %.15f" % k_1)
        print("k_2 = %.15f" % k_2)
        print("k_3 = %.15f" % k_3)
        print("k_4 = %.15f" % k_4)
        print("x_n = %.15f" % x_new)

        x.append(x_new)
        t += h

    print("x = %.15f" % x[-1])
    return x
