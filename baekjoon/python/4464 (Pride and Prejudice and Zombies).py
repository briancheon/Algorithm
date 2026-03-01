
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

def get_divisors(n):
    factors = factorize(n)
    counts = Counter(factors)

    prime_power_lists = []
    for prime, count in counts.items():
        prime_power_lists.append([prime**exp for exp in range(count + 1)])
        
    divisors = [1]
    for power_list in prime_power_lists:
        new_divisors = []
        for d in divisors:
            for factor in power_list:
                new_divisors.append(d * factor)
        divisors = new_divisors
    return sorted(set(divisors))

def is_vampire(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    original_sorted = sorted(s)
    low_bound = 10 ** (half - 1)
    high_bound = 10 ** half - 1

    divisors = get_divisors(n)
    for d in divisors:
        if d < low_bound or d > high_bound:
            continue
        fang2 = n // d

        if fang2 < low_bound or fang2 > high_bound:
            continue

        fang_str = str(d)
        fang2_str = str(fang2)

        if '00' in fang_str or '00' in fang2_str:
            continue

        combined = sorted(fang_str + fang2_str)
        if combined == original_sorted:
            return True

    return False

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    
    print(f'{N}: {"yes" if is_vampire(N) else "no"}')
