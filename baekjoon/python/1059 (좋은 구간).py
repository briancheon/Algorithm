import sys

L = int(sys.stdin.readline().rstrip())

S = sorted(map(int, sys.stdin.readline().split()))

n = int(sys.stdin.readline().rstrip())

if n not in S:
    A, B = 0, 0
    for num in S:
        if num < n:
            A = num
        if num > n:
            B = num
            break
    print((n - A - 1) * (B - n) + B - n - 1)

else:
    print(0)
