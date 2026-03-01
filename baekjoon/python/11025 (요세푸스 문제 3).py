import sys

N, K = map(int, sys.stdin.readline().split())

last = 0
for n in range(1, N + 1):
    last = (last + K) % n

print(last + 1)