import sys
import random
import time

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

def legendre(n):
    while True:
        if n % 4 == 0:
            n //= 4
        else:
            return True if n % 8 == 7 else False
        
def square(n):
    if int(n ** 0.5) ** 2 == n:
        return True
    
    return False

def fermat(n):
    flag = True
    factors = factorize(n)
    for base in factors:
        if (base + 1) % 4 == 0 and factors[base] % 2:
            flag = False
    return flag

def tonelli_shanks(n, p):
    q = p - 1
    s = 0
    while q % 2 == 0:
        s += 1
        q //= 2

    z = 2
    while pow(z, (p - 1) // 2, p) == 1:
        z += 1
    
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s

    while True:
        if t == 0:
            return 0
        
        if t == 1:
            return r

        k = t * t % p
        for i in range(1, m):
            if k == 1:
                break
            k = (k * k) % p
        
        b = pow(c, pow(2, m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i

def cornacchia(n):
    if n == 2:
        return 1, 1

    t = tonelli_shanks(n - 1, n)
    
    r1, r2 = n, t
    while r1 * r1 >= n:
        r1, r2 = r2, r1 % r2

    x = r1
    y = int((n - x * x) ** 0.5)
    
    return x, y

def sum_two_squares(n):
    factors = factorize(n)
    x, y = 0, 1
    base = 1
    for factor in factors:
        base *= pow(factor, factors[factor] // 2)
        if factors[factor] % 2:
            temp_x, temp_y = cornacchia(factor)
            x, y = x * temp_y + y * temp_x, abs(x * temp_x - y * temp_y)

    return x * base, y * base

def sum_three_squares(n):
    factors = factorize(n)
    base, check_n = 1, 1
    for factor, power in factors.items():
        base *= pow(factor, power // 2)
        check_n *= pow(factor, power % 2)

    t = 1
    while not fermat(check_n - t * t):
        t += 1

    x, y = sum_two_squares(check_n - t * t)

    return t * base, x * base, y * base

n = int(sys.stdin.readline().rstrip())

if square(n):
    print(1)
    print(int(n ** 0.5))

elif fermat(n):
    print(2)
    print(*sum_two_squares(n))

elif legendre(n):
    print(4)

    i = 0
    while n % 4 == 0:
        n //= 4
        i += 1

    t, x, y = sum_three_squares(n - 1)

    answer = map(lambda x: x * pow(2, i), [1, t, x, y])

    print(*answer)

else:
    print(3)
    print(*sum_three_squares(n))