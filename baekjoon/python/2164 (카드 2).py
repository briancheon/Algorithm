import sys
from collections import deque

def cards(n):
    q = deque(range(1, n + 1))
    while len(q) > 1:
        q.popleft()
        q.append(q.popleft())

    return q[0]


N = int(sys.stdin.readline().rstrip())

print(cards(N))

