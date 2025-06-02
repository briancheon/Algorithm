import sys

def fib(n):
    x, y = 0, 1
    for c in range(n):
        x, y = y, x + y
    return x


N = int(sys.stdin.readline().rstrip())
print(fib(N) % 1000000)