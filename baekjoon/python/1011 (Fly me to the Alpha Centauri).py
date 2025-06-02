import sys

def smallest_square(n):
    if int(n ** 0.5) ** 2 == n:
        return n
    else:
        return (int(n ** 0.5) + 1) ** 2

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    length = y - x
    s = smallest_square(length)
    if length > s - s ** 0.5:
        print(2 * int(s ** 0.5) - 1)
    else:
        print(2 * int(s ** 0.5) - 2)
