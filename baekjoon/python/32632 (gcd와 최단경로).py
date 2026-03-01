import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

K, N = map(int, sys.stdin.readline().split())

cnt = 0
for x in range(1, N + 1):
    if x == K:
        continue

    check = gcd(x, K)
    if check == 1 or check == 2:
        cnt += 1

print(cnt)