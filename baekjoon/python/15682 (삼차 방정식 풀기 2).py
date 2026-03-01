import sys
from decimal import getcontext, Decimal

getcontext().prec = 100

def bisection_method(func, a, b, tolerance='1.0e-20'):
    a, b = Decimal(a), Decimal(b)
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

    return x

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    A, B, C, D = map(Decimal, sys.stdin.readline().split())
    f = lambda x: A * x ** 3 + B * x ** 2 + C * x + D
    f_prime = lambda x: 3 * A * x ** 2 + 2 * B * x + C
    p_discriminant = B ** 2 - 3 * A * C

    if p_discriminant >= 0:
        p = (-B - p_discriminant ** Decimal(0.5)) / (3 * A)
        q = (-B + p_discriminant ** Decimal(0.5)) / (3 * A)
        if p > q:
            p, q = q, p
        
        if round(f(p) * f(q), 20) > 0:
            roots = [bisection_method(f, -1000000, 1000000)]
        
        elif round(f(p), 20) == 0 or round(f(q), 20) == 0:
            if round(f(p), 20) == 0:
                if round(p, 20) == round(q, 20):
                    roots = [p]   
                else:
                    roots = [p, bisection_method(f, q, 1000000)]
            
            else:
                roots = [bisection_method(f, -1000000, p), q]
            
        else:
            ranges = [(-1000000, p), (p, q), (q, 1000000)]
            roots = list(map(lambda x: bisection_method(f, *x), ranges))

    else:
        roots = [bisection_method(f, -1000000, 1000000)]
    
    print(*map(lambda x: f'{x:.20f}',roots), sep=' ')