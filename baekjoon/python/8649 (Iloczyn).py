import sys
import random

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0:
        return False
    
    s, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break

        else:
            return False
        
    return True

def rho(n):
    def f(x, c):
        return (x * x % n + c) % n

    if n == 1:
        return 1

    if miller_rabin(n):
        return n

    if n % 2 == 0:
        return 2

    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        if n % p == 0:
            return p

    x = random.randrange(2, n)
    c = random.randrange(1, n)
    y = x
    d = 1

    while d == 1:
        x = f(x, c)
        y = f(f(y, c), c)

        d = gcd(abs(x - y), n)
        if d == n:
            return rho(n)

    if miller_rabin(d):
        return d

    return rho(d)

def factorize(n):
    factors = {}
    while n > 1:
        factor = rho(n)
        count = 0
        while n % factor == 0:
            count += 1
            n //= factor
        factors[factor] = count
    return factors

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    if k == 1:
        print("TAK")

        
