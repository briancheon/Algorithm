import sys


def arrange(x):
    a, b, p, q = x
    if a > b:
        return [b, a, q, p]
    return x


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


N = int(sys.stdin.readline())

mass, ratios = [1] * N, []

for c in range(N - 1):
    ratios.append(list(map(int, sys.stdin.readline().split())))

ratios = sorted(list(map(arrange, ratios)))

divisor = mass[0]
for c in range(N):
    divisor = gcd(divisor, mass[c])

mass = list(map(lambda x: x // divisor, mass))
print(*mass, sep=' ')




