import sys
import random

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
    if n == 1:
        return 1

    if miller_rabin(n):
        return n

    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        if n % p == 0:
            return p

    x = random.randrange(2, n)
    c = random.randrange(1, n)
    y = x
    d = 1

    f = lambda x: (x * x % n + c) % n

    while d == 1:
        x = f(x)
        y = f(f(y))

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
        factors[factor] = 1 << count
    return factors

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

memo = {}
def G(state):
    if state in memo:
        return memo[state]

    if state == 0:
        memo[state] = 0
        return 0

    temp = set()
    max_k = state.bit_length()

    for k in range(1, max_k):
        below_k = state & ((1 << k) - 1)
        above_k = state >> k
        above_k &= ~1

        new_state = below_k | above_k

        temp.add(G(new_state))

    memo[state] = mex(temp)
    return memo[state]

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

factor_powers = {}
for Ai in A:
    for p, cnt in factorize(Ai).items():
        factor_powers[p] = factor_powers.get(p, 0) | cnt

nim_sum = 0
for powers in factor_powers.values():
    nim_sum ^= G(powers)

print("koosaga" if nim_sum else "cubelover")