import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    num = x = int(sys.stdin.readline().rstrip())
    while not is_prime(x):
        x += 1

    print(x)
