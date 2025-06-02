import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

S = defaultdict(int)

for c in range(N):
    string = sys.stdin.readline().rstrip()
    S[string] = 1

count = 0
for c in range(M):
    string = sys.stdin.readline().rstrip()
    count += S[string]

print(count)
