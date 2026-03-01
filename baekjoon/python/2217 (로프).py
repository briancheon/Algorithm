import sys

N = int(sys.stdin.readline().rstrip())
ropes = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
ropes.sort(reverse=True)

maximum_weight = 0
for i in range(N):
    if ropes[i] * (i + 1) > maximum_weight:
        maximum_weight = ropes[i] * (i + 1)

print(maximum_weight)