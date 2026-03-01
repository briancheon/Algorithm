import sys

def factors(n):
    f = []
    for i in range(1, n + 1):
        if n % i == 0:
            f.append(i)
    return f

def int_root(a, b, c, d):
    if d == 0:
        return 0
    for r in factors(abs(d)):
        if a * r ** 3 + b * r ** 2 + c * r == -d:
            return r
        elif -a * r ** 3 + b * r ** 2 - c * r == -d:
            return -r

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    A, B, C, D = map(int, sys.stdin.readline().split())
    integer_root = int_root(A, B, C, D)
    n_A, n_B, n_C = A, B + A * integer_root, C + B * integer_root + A * integer_root ** 2
    roots = {integer_root}
    
    disciminant = n_B ** 2 - 4 * n_A * n_C
    if disciminant > 0:
        roots.add((-n_B + disciminant ** 0.5) / (2 * n_A))
        roots.add((-n_B - disciminant ** 0.5) / (2 * n_A))
    elif disciminant == 0:
        roots.add(-n_B / (2 * n_A))
    
    roots = sorted(roots)
    print(*map(lambda x: f'{x:.4f}',roots), sep=' ')