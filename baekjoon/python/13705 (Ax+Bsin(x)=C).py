import sys
from decimal import getcontext, Decimal, ROUND_HALF_UP

getcontext().prec = 50
getcontext().rounding = ROUND_HALF_UP

def sin(x):
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    return s


def bisection_method(func, a, b, tolerance='1.0e-21'):
    x, dx = Decimal('0'), abs(b - a)
    while Decimal(dx) > Decimal(tolerance):
        x = (a + b) / Decimal('2.0')
        if abs(func(x)) < Decimal(tolerance):
            break
        elif func(a) * func(x) < 0:
            b = x
        else:
            a = x
        dx = abs(b - a)

    return round(x, 6)

PI = Decimal('3.14159265358979323846264338327950288419716939937510')

A, B, C = map(Decimal, sys.stdin.readline().split())

f = lambda x: A * x + B * sin(x % (2 * PI)) - C

print(bisection_method(f, Decimal('0'), (C + B + 1) / A))
