import sys

def P(n):
    if n <= 3:
        return 1
    elif n <= 5:
        return 2

    p = [1, 1, 1, 2, 2] + [0] * (n - 5)
    for i in range(5, n):
        p[i] = p[i - 1] + p[i - 5]

    return p[-1]


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(P(N))
