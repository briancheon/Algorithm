import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())
heart_rate = m
time = 0

if m + T > M:
    print(-1)
else:
    while N > 0 and m <= heart_rate <= M:
        if heart_rate + T <= M:
            heart_rate += T
            N -= 1
        elif heart_rate - R >= m:
            heart_rate = heart_rate - R
        else:
            heart_rate = m

        time += 1

    print(time)
