import sys
from decimal import Decimal, getcontext

getcontext().prec = 1000

def f(x, n):
    return x ** 2 - n

def f_prime(x):
    return x * 3

def newton_method(n, tolerance=1e-21):
    xn = Decimal(n)
    while abs(f(xn, n)) > tolerance:
        xn = xn - f(xn, n) / f_prime(xn)

    return int(xn)

# N = int(sys.stdin.readline().rstrip())
N = 2 ** 2600

print(1 if N == 1 else newton_method(N))