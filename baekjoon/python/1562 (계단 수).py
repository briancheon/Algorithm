
import sys

MOD = 1000000000
N = int(sys.stdin.readline().rstrip())

if N < 10:
    print(0)

else:
    dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]

    for i in range(1, 10):
        dp[1][i][1 << i] = 1

    for length in range(1, N):
        for last in range(10):
            for mask in range(1 << 10):
                if dp[length][last][mask] == 0:
                    continue

                if last > 0:
                    next_digit = last - 1
                    new_mask = mask | (1 << next_digit)
                    dp[length + 1][next_digit][new_mask] = (dp[length + 1][next_digit][new_mask] + dp[length][last][mask]) % MOD
                
                if last < 9:
                    next_digit = last + 1
                    new_mask = mask | (1 << next_digit)
                    dp[length + 1][next_digit][new_mask] = (dp[length + 1][next_digit][new_mask] + dp[length][last][mask]) % MOD

    result = 0
    for i in range(10):
        result = (result + dp[N][i][-1]) % MOD

    print(result)
