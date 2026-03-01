import sys
import random

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def miller_rabin(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 3, 5, 7, 11]:
        if a >= n:
            continue
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
    if n % 2 == 0:
        return 2
    
    if n % 3 == 0:
        return 3
    
    if n % 5 == 0:
        return 5
    
    while True:
        c = random.randrange(1, n)
        f = lambda x: (pow(x, 2, n) + c) % n
        x, y, d = 2, 2, 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
        
        if d != n:
            return d

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

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    if N == 1 or N == 4:
        print(1)
        continue

    factors = factorize(N)
    