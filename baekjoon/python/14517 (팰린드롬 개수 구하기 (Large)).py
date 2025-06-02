
import sys

MOD = 10007

dp = [[-1] * 1001 for _ in range(1001)] 

def palindrome_count(s, start, end):
    global dp
    cnt = 0
    if dp[start][end] != -1:
        return dp[start][end]
    
    if start == end:
        dp[start][end] = 1
        return 1
    
    if end < start:
        dp[start][end] = 0
        return 0
    
    if s[start] == s[end]:
        cnt += palindrome_count(s, start + 1, end - 1) + 1

    cnt += (palindrome_count(s, start + 1, end) + palindrome_count(s, start, end - 1) - palindrome_count(s, start + 1, end - 1) + MOD) % MOD
    cnt %= MOD

    dp[start][end] = cnt
    return cnt
    
S = sys.stdin.readline().rstrip()

print(palindrome_count(S, 0, len(S) - 1))
