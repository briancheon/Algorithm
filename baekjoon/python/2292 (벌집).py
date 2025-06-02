from math import sqrt, ceil

N = int(input())

if N == 1:
    n1 = 1
else:
    n1 = ceil((3 + sqrt(9 + 12 * (N - 1))) / 6)

print(n1)
