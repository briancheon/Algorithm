import sys

N = int(sys.stdin.readline().rstrip())

times = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

times.sort(key=lambda x: (x[1], x[0]))

x = times.pop(0)[1]
count = 1

for c in times:
    if c[0] >= x:
        count += 1
        x = c[1]

print(count)