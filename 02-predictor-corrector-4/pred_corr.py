#!/usr/bin/python3
import math

def pred_corr(f, t_0, x_0, h, n, target_eps):
    print("t_0 = %.15f" % t_0)
    print("x_0 = %.15f" % x_0)
    print("h   = %.15f" % h)
    print("n   = %d" % n)

    x_n = [x_0]
    eps_n = [0.0]
    h_n = []
    t = t_0
    i = 0

    while n > 0:
        x_14_2 = x_n[-1] + h/4 * f(t, x_n[-1])
        x_12_3 = x_n[-1] + h/2 * f(t + h/4, x_14_2)
        x_11_3 = x_n[-1] + h/1 * f(t + h/2, x_12_3)
        x_11_4 = x_n[-1] + h/6 * (f(t, x_n[-1]) +
                                  4 * f(t + h/2, x_12_3) +
                                  f(t + h, x_11_3))

        local_eps = (x_11_4 - x_11_3)

        if (abs(local_eps) > target_eps):
            n *= 2
            h /= 2
            i += 1
            continue

        print("-" * 30)
        print("step %d" % (i + 1))
        print("t      = %.15f" % x_n[-1])
        print("x_n    = %.15f" % x_n[-1])
        print("x_14_2 = %.15f" % x_14_2)
        print("x_12_3 = %.15f" % x_12_3)
        print("x_11_3 = %.15f" % x_11_3)
        print("x_11_4 = %.15f" % x_11_4)
        print("x_n+1  = %.15f" % x_11_4)
        print("eps    = %.15f" % local_eps)
        # input("Anykey...")

        eps_n.append(x_11_3 - x_11_4)
        x_n.append(x_11_4)
        h_n.append(h)
        t += h
        n -= 1
        i += 1

    print("x_n = %.15f" % x_n[-1])
    return (x_n, h_n, eps_n)
