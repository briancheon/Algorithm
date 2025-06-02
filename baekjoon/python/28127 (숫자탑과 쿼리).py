import sys

Q = int(sys.stdin.readline().rstrip())

for _ in range(Q):
    a, d, x = map(int, sys.stdin.readline().split())
    
    n = int((d - 2 * a + ((2 * a - d) ** 2 + 8 * d * x) ** 0.5) / (2 * d))
    
    if x == n * (2 * a + (n - 1) * d) / 2:
        print(n, a + (n - 1) * d)
    else:
        print(n + 1, int(x - n * (2 * a + (n - 1) * d) / 2))