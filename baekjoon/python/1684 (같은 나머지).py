import sys

n = int(sys.stdin.readline().rstrip())
_n = sorted(list(map(int, sys.stdin.readline().split())))

answer = 1

for c in range(abs(_n[0]), 1, -1):
    check = list(map(lambda x: x % c, _n))
    if check.count(check[0]) == len(check):
        answer = c
        break

print(answer)
