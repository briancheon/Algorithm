import sys

def ceil(n):
    if int(n) == n:
        return int(n)
    return int(n) + 1

N = int(sys.stdin.readline().rstrip())
t_shirts = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

print(sum(map(lambda x: ceil(x / T), t_shirts)))
print(N // P, N % P)
