#!/usr/bin/python3
import math

VERBOSE = False

def fin_diff(phi, phi_xx, psi, mu_0, mu_1, f,
             x_0, x_1, t_0, t_1,
             x_count, t_count):
    h = (x_1 - x_0) / x_count
    tau = (t_1 - t_0) / t_count

    if x_count < 0 or t_count < 0:
        raise ArgumentError("x_count and t_count must be positive")
    if x_count == 0:
        return [mu_0(t_1), mu_1(t_1)]

    y = [[0.0] * (x_count + 1) for i in range(3)]

    for m in range(x_count + 1):
        y[0][m] = phi(x_0 + h * m)

    for m in range(1, x_count):
        y[1][m] = (y[0][m] +
                   tau * psi(x_0 + h * m) +
                   0.5 * tau ** 2 * phi_xx(x_0 + h * m))
    y[1][0] = mu_0(t_0 + tau)
    y[1][x_count] = mu_1(t_0 + tau)

    # if VERBOSE:
        # for n in range(2):
            # print("-" * 30)
            # print("n = %d" % n)
            # print("t = %f" % (t_0 + tau * n))
            # print("y =", y[n])
            # input("")

    if t_count == 0:
        return y[1]

    for n in range(2, t_count + 1):
        t_local = t_0 +  tau * n
        for m in range(1, x_count):
            y[2][m] = (tau ** 2 / h ** 2 * (y[1][m-1] + y[1][m+1]) +
                       2 *(1 - tau ** 2 / h ** 2) * y[1][m] -
                       1 * y[0][m]
                       + tau ** 2 * f(x_0 + h * m, t_local))
        y[2][0] = mu_0(t_local)
        y[2][x_count] = mu_1(t_local)

        # if VERBOSE:
            # print("-" * 30)
            # print("n = %d" % n)
            # print("t = %f" % t_local)
            # print("y =", y[2])
            # input("")

        y[:] = y[1], y[2], y[0]

    return y[1]
