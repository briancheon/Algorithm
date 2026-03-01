import sys

S = sys.stdin.readline().rstrip()
n = len(S)

palindrome = [[0] * n for _ in range(n)]

for i in range(n):
    palindrome[i][i] = 1

for i in range(n - 1):
    if S[i] == S[i + 1]:
        palindrome[i][i + 1] = 1

for length in range(3, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if S[i] == S[j] and palindrome[i + 1][j - 1]:
            palindrome[i][j] = 1

dp = [float('inf')] * n
for i in range(n):
    if palindrome[0][i]:
        dp[i] = 1
    else:
        for j in range(i):
            if palindrome[j + 1][i]:
                dp[i] = min(dp[i], dp[j] + 1)
                
print(dp[n - 1])