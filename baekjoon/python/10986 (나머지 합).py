import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))

for c in range(1, N + 1):
    nums[c] = (nums[c - 1] + nums[c]) % M

nums = Counter(nums)
answer = 0

for n in nums.keys():
    answer += nums[n] * (nums[n] - 1) // 2

print(answer)

