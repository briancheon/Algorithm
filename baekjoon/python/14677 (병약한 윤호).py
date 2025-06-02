import sys

dp = [[-1] * 1501 for _ in range(1501)]
def maximum_count(med, l, r, c):
    if l > r:
        return 0
    
    if dp[l][r] != -1:
        return dp[l][r]

    cur = "BLD"[c]
    if med[l] != cur and med[r] != cur:
        return 0
    
    cnt = 1
    
    if med[l] == cur and med[r] == cur:
        cnt += max(maximum_count(med, l + 1, r, (c + 1) % 3), maximum_count(med, l, r - 1, (c + 1) % 3))
    
    elif med[l] == cur:
        cnt += maximum_count(med, l + 1, r, (c + 1) % 3)
    
    elif med[r] == cur:
        cnt += maximum_count(med, l, r - 1, (c + 1) % 3)
        
    dp[l][r] = cnt
    return dp[l][r]

N = int(sys.stdin.readline().rstrip())
medicine = sys.stdin.readline().rstrip()

print(maximum_count(medicine, 0, 3 * N - 1, 0))