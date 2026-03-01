import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

valid_min = 1

freq = defaultdict(int)

for i in range(N):
    candidate = A[i] - i * K
    if candidate >= valid_min:
        freq[candidate] += 1

max_count = max(freq.values()) if freq else 0

min_operations = N - max_count
print(min_operations)