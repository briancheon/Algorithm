import sys

N = int(sys.stdin.readline().rstrip())
stairs = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

if N <= 2:
    print(sum(stairs[:N]))

elif N == 3:
    print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

else:
    dp = [0] * (N + 1)
    dp[1] = stairs[0]
    dp[2] = stairs[0] + stairs[1]
    dp[3] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(4, N + 1):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i - 2], dp[i - 2] + stairs[i - 1])

    print(dp[N])