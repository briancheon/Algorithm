import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    dp = [float('inf')] * 100001
    dp[0] = 0

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        for i in range(100000, -1, -1):
            if i >= a:
                dp[i]  = min(dp[i] + b, dp[i - a])
            else:
                dp[i] += b

    ans = float('inf')
    for i in range(100001):
        ans = min(ans, max(dp[i], i))

    print(ans)