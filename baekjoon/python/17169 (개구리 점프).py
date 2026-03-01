import sys

def possible(arr, i1, i2):


N, Q = map(int, sys.stdin.readline().split())

logs = [list(map(int, sys.stdin.readline().split())[:-1]) for _ in range(N)]
sorted_logs = sorted(logs, key=lambda x: (x[0], x[1]))

for c in range(Q):
    l1, l2 = map(int, sys.stdin.readline().split())
    print(possible(sorted_logs, l1, l2))
