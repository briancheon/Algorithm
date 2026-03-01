import sys

N = int(sys.stdin.readline().rstrip())
dp = list(range(N + 1))

squares = [i * i for i in range(1, int(N ** 0.5) + 1)]

for i in range(1, N + 1):
    for s in squares:
        if s > i:
            break

        if dp[i] > dp[i - s] + 1:
            dp[i] = dp[i - s] + 1

print(dp[N])