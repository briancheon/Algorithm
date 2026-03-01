import sys

def max_score(arr, arr_sum, left, right):
    if left == right:
        dp[left][right] = arr[left]
        return dp[left][right]
    
    if dp[left][right] != 0:
        return dp[left][right]
    
    dp[left][right] = max(arr[left] + arr_sum[right + 1] - arr_sum[left + 1] - max_score(arr, arr_sum, left + 1, right), \
                          arr[right] + arr_sum[right] - arr_sum[left] - max_score(arr, arr_sum, left, right - 1))

    return dp[left][right]

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    cards = list(map(int, sys.stdin.readline().split()))

    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + cards[i - 1]

    dp = [[0] * N for _ in range(N)]

    print(max_score(cards, prefix_sum, 0, N - 1))