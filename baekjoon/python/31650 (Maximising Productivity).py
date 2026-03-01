import sys

N, Q = map(int, sys.stdin.readline().split())

c = list(map(int, sys.stdin.readline().split()))
t = list(map(int, sys.stdin.readline().split()))

diff = sorted([c[i] - t[i] for i in range(N)], reverse=True)

for _ in range(Q):
    V, S = map(int, sys.stdin.readline().split())

    if diff[V - 1] > S:
        print("YES")
    else:
        print("NO")