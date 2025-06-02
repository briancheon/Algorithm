import sys
import random

def miller_rabin(n, s=5):
    if n == 2:
        return True
      
    elif n % 2 == 0:
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

    for i in range(t):
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
    
    x = random.randrange(2, n)
    c = random.randrange(1, n)
    d = 1
    y = x
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
        return []
    
    if miller_rabin(n):
        return [n]
    
    factor = rho(n)
    return factorize(factor) + factorize(n // factor)

N = int(sys.stdin.readline().strip())
print(*sorted(factorize(N)), sep='\n')