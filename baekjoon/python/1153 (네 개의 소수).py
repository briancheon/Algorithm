import time


def sieve(n):
    primes = [True for c in range(n + 1)]
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for c in range(p ** 2, n + 1, p):
                primes[c] = False
        p += 1
    primes[0] = primes[1] = False
    return list(filter(lambda x: primes[x], [i for i, _ in enumerate(primes)]))


start = time.time()
a = sieve(10 ** 6)
print(time.time() - start)




