import sys

N = int(sys.stdin.readline().rstrip())

coordinates = []

for c in range(N):
    coordinates.append(list(map(int, sys.stdin.readline().split())))

coordinates.sort(key=lambda x: (x[0], x[1]))

for c in coordinates:
    print(c[0], c[1])
