import sys
from random import randrange

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def miller_rabin(n):
    if n < 2:
        return False
    
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    s = 0
    while not d & 1:
        d >>= 1
        s += 1

    bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
    for a in bases:
        if a % n == 0:
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
        
    x = randrange(2, n)
    c = randrange(1, n)
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
    factors = set()
    while n > 1:
        factor = rho(n)
        while n % factor == 0:
            n //= factor
        factors.add(factor)
    return factors

n = int(sys.stdin.readline().rstrip())
a = list(map(lambda x: factorize(int(x)), sys.stdin.readline().split()))

all_factors = set().union(*a)

nim_sum = 0
while all_factors:
    factor = all_factors.pop()
    temp_nim = 0
    for ai in a:
        if factor in ai:
            temp_nim += 1

        else:
            nim_sum ^= temp_nim
            temp_nim = 0
            
    nim_sum ^= temp_nim

print("First" if nim_sum else "Second")