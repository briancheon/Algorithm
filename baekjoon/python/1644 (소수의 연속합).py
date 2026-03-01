import sys

N = int(sys.stdin.readline().rstrip())

if N < 2:
    print(0)

else:
    sieve = list(range(N + 1))
    sieve[1] = 0

    for i in range(2, int((N + 1) ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                sieve[j] = 0

    primes = list(filter(lambda x: x, sieve))

    cnt = cur_sum = 0
    left = 0
    right = 0

    while True:
        if cur_sum >= N:
            if cur_sum == N:
                cnt += 1
            cur_sum -= primes[left]
            left += 1

        else:
            if right == len(primes):
                break
            cur_sum += primes[right]
            right += 1

    print(cnt)