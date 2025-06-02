import sys

N, M = map(int, sys.stdin.readline().split())

def euler_phi(n):
    phi = n

    if n % 2 == 0:
        phi -= phi // 2
        while n % 2 == 0:
            n //= 2

    p = 3
    while p * p <= n:
        if n % p == 0:
            phi -= phi // p
            while n % p == 0:
                n //= p
        p += 2

    if n > 1:
        phi -= phi // n

    return phi

def exponial(n, m):
    if m == 1:
        return 0
    
    if n == 1:
        return 1
    
    if n < 4:
        return pow(n, n - 1, m)
    
    if n == 4:
        return 262144

    return pow(n, exponial(n - 1, euler_phi(m)) + euler_phi(m), m)

print(exponial(N, M) % M)