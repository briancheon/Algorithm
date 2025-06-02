import sys

def continuous(n):
    count = 0
    i = 2

    while i * (i - 1) // 2 < n:
        a = n - i * (i - 1) // 2
        if a > 0 and a % i == 0:
            count += 1
        i += 1
    return count

T = int(sys.stdin.readline().rstrip())
ls = [int(sys.stdin.readline().rstrip()) for _ in range(T)]

print(*map(continuous, ls), sep='\n')