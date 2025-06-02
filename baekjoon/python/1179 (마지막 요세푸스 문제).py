import sys

N, K = map(int, sys.stdin.readline().split())

answer = 0
temp = 1

if K == 1:
    print(N)

else:
    while True:
        x = (temp - answer - 1) // (K - 1) + 1
        if temp + x > N:
            answer += (N - temp) * K
            break

        answer = (answer + K * x) % (temp + x)
        temp += x

    print(answer + 1)