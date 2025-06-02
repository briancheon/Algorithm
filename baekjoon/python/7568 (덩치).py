import sys


def compare(x, y, p, q):
    if x > p and y > q:
        return 0, 1
    elif x < p and y < q:
        return 1, 0
    return 0, 0


N = int(sys.stdin.readline().rstrip())

data = []
people = [1] * N
for c in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(N - 1):
    for j in range(i + 1, N):
        add = compare(*data[i], *data[j])
        people[i] += add[0]
        people[j] += add[1]

print(*people, sep=' ')
