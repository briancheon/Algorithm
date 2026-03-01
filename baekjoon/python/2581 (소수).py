import sys

def isPrime(n):
    if n == 1:
        return False
    elif n <= 3:
        return True

    x = 2
    while x <= n ** 0.5:
        if n % x == 0:
            return False
        x += 1
    return True

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

if M % 2 == 0 and M > 2:
    M += 1

primes = []

for num in range(M, N + 1, 2):
    if isPrime(num):
        primes.append(num)

if len(primes):
    print(sum(primes))
    print(primes[0])
else:
    print(-1)


