import sys
from random import randrange

def miller_rabin(n, k=5):
    if n < 2:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0:
        return False
    
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = randrange(2, n - 1)
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

A, B = map(int, sys.stdin.readline().split())

for n in range(A, B + 1):
    if miller_rabin(n) or n == 9:
        print(n, end=' ')