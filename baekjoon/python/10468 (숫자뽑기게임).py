import sys

def find(arr, left, right, dp):
    if dp[left][right] != -1:
        return dp[left][right]
    
    if left >= right:
        dp[left][right] = 0
        return 0
    
    ans = 0
    for i in range(left + 1, right):
        ans = max(ans, find(arr, left, i, dp) + find(arr, i, right, dp) + arr[left] + arr[i] + arr[right])

    dp[left][right] = ans
    return ans

while True:
    n, *k = map(int, sys.stdin.readline().split())
    if n == 0:
        break

    dp = [[-1] * 201 for _ in range(201)]
    print(find(k, 0, n - 1, dp))
