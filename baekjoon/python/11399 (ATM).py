import sys

N = int(sys.stdin.readline().rstrip())

nums = [0] + list(map(int, sys.stdin.readline().split()))

nums.sort()

for c in range(1, N + 1):
    nums[c] += nums[c - 1]

print(sum(nums))
