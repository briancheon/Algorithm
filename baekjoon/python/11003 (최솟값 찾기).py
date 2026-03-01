import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

D = deque()

for i in range(N):
    if D and D[0][0] <= i - L:
        D.popleft()
    
    while D and A[i] < D[-1][1]:
        D.pop()
        
    D.append((i, A[i]))
    
    print(D[0][1], end=' ')