import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().rstrip())

a.sort()
l, r = 0, n - 1
count = 0

while l < r:
    if a[l] + a[r] == x:
        count += 1
        l += 1
        r -= 1
    elif a[l] + a[r] < x:
        l += 1
    else:
        r -= 1

print(count)