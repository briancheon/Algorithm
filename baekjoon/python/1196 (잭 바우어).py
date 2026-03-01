import sys
from decimal import Decimal, getcontext

getcontext().prec = 1000

EULER = Decimal("0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495")

def harmonic(n):
    if n <= 1000000:
        answer = Decimal(0)
        for i in range(1, n + 1):
            answer += Decimal(1) / Decimal(i)
        return answer
    
    n = Decimal(n)
    n2 = n * n
    n4 = n2 * n2
    n6 = n4 * n2
    return n.ln() + EULER + Decimal(1) / (2 * n) - Decimal(1) / (12 * n2) + Decimal(1) / (120 * n4) - Decimal(1) / (252 * n6)

N, K = map(int, sys.stdin.readline().split())

if N == 1:
    print(1)

elif K <= 1000000:
    answer = Decimal(0)
    for i in range(N - K + 1, N + 1):
        answer += Decimal(N) / Decimal(i)
    print(answer)

elif N - K == 0:
    print(Decimal(N) * harmonic(N))

elif K <= N // 10:
    N, K = Decimal(N), Decimal(K)
    M = N - K
    answer = N * (N / M).ln() + Decimal(N) / (2 * N) - Decimal(N) / (12 * N * N) + Decimal(N) / (120 * N * N * N * N) - Decimal(N) / (2 * M) + Decimal(N) / (12 * M * M) - Decimal(N) / (120 * M * M * M * M)
    print(answer)

else:
    print(Decimal(N) * (harmonic(N) - harmonic(N - K)))