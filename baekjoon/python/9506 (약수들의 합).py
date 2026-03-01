import sys

while 1:
    n = int(sys.stdin.readline().rstrip())

    if n < 0:
        break

    factors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)

    if sum(factors) == n:
        print(f"{n} = {' + '.join(map(str, factors))}")
    else:
        print(f"{n} is NOT perfect.")




