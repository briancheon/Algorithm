import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline().rstrip())

for i in range(N - 1):
    if S <= 0:
        break
    m, idx = nums[i], i
    for j in range(i, min(N, i + S + 1)):
        if m < nums[j]:
            m = nums[j]
            idx = j

    S -= (idx - i)

    for j in range(idx, i, -1):
        nums[j] = nums[j - 1]
    nums[i] = m

print(*nums)
