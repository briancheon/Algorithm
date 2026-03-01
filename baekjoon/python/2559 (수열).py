import sys


def maximum(l, n, k):
    if n == 1:
        return max(l)
    else:
        m = check = sum(l[0:k])
        for c in range(n - k):
            check += -l[c] + l[c + k]
            if check > m:
                m = check
        return m


N, K = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))

print(maximum(ls, N, K))
