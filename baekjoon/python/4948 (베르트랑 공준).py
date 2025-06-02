import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 1

while n != 0:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    count = 0
    for c in range(n + 1, 2 * n + 1):
        if is_prime(c):
            count += 1
    print(count)
