import sys

primes = []
checked = [0] * 1000001
checked[0] = 1
checked[1] = 1

for i in range(2, 1000001):
    if checked[i] == 0:
        primes.append(i)
        for j in range(2 * i,  1000001, i):
            checked[j] = 1

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    count = 0
    for prime in primes:
        if prime >= N // 2:
            break
        if not checked[N - prime] and prime <= N - prime:
            count += 1

    print(count)
