import sys
import random

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
    factors = {}
    while n > 1:
        factor = rho(n)
        count = 0
        while n % factor == 0:
            count += 1
            n //= factor
        factors[factor] = count
    return factors

def next_version(powers, primes, N):
    for i in range(len(powers) - 1, -1, -1):
        check = powers[:]
        check[i] += 1
        for j in range(i + 1, len(powers)):
            check[j] = 1

        product = 1
        for p, exp in zip(primes, check):
            product *= p ** exp

            if product > N:
                break

        if product <= N:
            return product
        
    return None

a, N = map(int, sys.stdin.readline().split())

factors = factorize(a)
primes = sorted(factors.keys())
powers = [factors[p] for p in primes]

check_num = next_version(powers, primes, N)
if check_num is None:
    print(-1)
else:
    print(check_num)