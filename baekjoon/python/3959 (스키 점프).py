import sys
from math import acos, pi

g = 9.81

def f(j, h, p, l):
    return -(l * l) / (4 * j) + h + p

def f_prime(j, h, p, l):
    return -l / (2 * j)

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    J, P, H, L = map(int, sys.stdin.readline().split())
    v0 = (2 * g * J) ** 0.5
    check = f(J, H, P, L / 2)
    if check < H / 2:
        I = (P / (1 / (4 * J) - (2 * H) / (L * L))) ** 0.5
        tangent = (1, -4 * H * I / (L * L))

    elif check == H / 2:
        I = L / 2
        tangent = (1, -4 * H * I / (L * L))

    elif H / 2 < check and f(J, H, P, L) < 0:
        A = (2 * H) / (L * L) + 1 / (4 * J)
        B = -(4 * H) / L
        C = H - P
        I = (-B + (B * B - 4 * A * C) ** 0.5) / (2 * A)
        tangent = (1, (4 * H / L) * (I / L - 1))

    else:
        I = 2 * ((J * (H + P)) ** 0.5)
        tangent = (1, 0)

    v = (v0 ** 2 + 2 * g * (H + P) - 2 * g * f(J, H, P, I)) ** 0.5

    v_vector = (1, f_prime(J, H, P, I))

    alpha = acos((v_vector[0] * tangent[0] + v_vector[1] * tangent[1]) / (((v_vector[0] ** 2 + v_vector[1] ** 2) ** 0.5) * ((tangent[0] ** 2 + tangent[1] ** 2) ** 0.5))) * 180 / pi

    print(I, v, alpha)