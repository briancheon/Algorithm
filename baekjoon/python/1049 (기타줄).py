import sys

N, M = map(int, sys.stdin.readline().split())

minimum_p, minimum_s = float('inf'), float('inf')

for _ in range(M):
    p, s = map(int, sys.stdin.readline().split())
    if p < minimum_p:
        minimum_p = p
    if s < minimum_s:
        minimum_s = s

if minimum_s * 6 < minimum_p:
    print(minimum_s * N)
elif (N % 6) * minimum_s > minimum_p:
    print(minimum_p * (N // 6 + 1))
else:
    print(minimum_p * (N // 6) + minimum_s * (N % 6))


