# Pisano Period
import sys

Q, M = map(int, sys.stdin.readline().split())

fib_music = ""
i = 1

x, y = 1, 1
while x != 0 or y != 1:
    fib_music += str(x)
    x, y = y, (x + y) % M

fib_music += str(x)

n = len(fib_music)

for _ in range(Q):
    N = int(sys.stdin.readline().rstrip())
    print(fib_music[(N - 1) % n])