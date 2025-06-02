import sys

S1 = sys.stdin.readline().rstrip()
S2 = sys.stdin.readline().rstrip()

dp = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

for i in range(len(S1)):
    for j in range(len(S2)):
        if S1[i] == S2[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1

print(max(map(max, dp)))