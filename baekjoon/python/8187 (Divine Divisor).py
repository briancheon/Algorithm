import sys
import random
from collections import Counter

def miller_rabin(n, s=5):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for _ in range(s):
        a = random.randint(1, n - 1)
        if test(a, n):
            return False

    return True

def test(a, n):
    t = 0
    u = n - 1

    while u % 2 == 0:
        t += 1
        u //= 2

    preX = pow(a, u, n)
    curX = 0

    for _ in range(t):
        curX = (preX * preX) % n
        if curX == 1 and preX != 1 and preX != n - 1:
            return True
        preX = curX
        
    if curX != 1:
        return True

    return False

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def rho(n):
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
        x = (x * x % n + c) % n
        y = (y * y % n + c) % n
        y = (y * y % n + c) % n
        d = gcd(n, abs(x - y))
        if d == n:
            return rho(n)
        
    if miller_rabin(d):
        return d
    else:
        return rho(d)

def factorize(n):
    if n == 1:
        return ()
    if miller_rabin(n):
        return (n,)
    factor = rho(n)
    return factorize(factor) + factorize(n // factor)

_ = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))

N_factorized = Counter(factor for a in A for factor in factorize(a))

max_count = max(N_factorized.values())
max_prime_count = sum(1 for count in N_factorized.values() if count == max_count)

divine_divisor_count = 2 ** max_prime_count - 1

print(max_count)
print(divine_divisor_count)