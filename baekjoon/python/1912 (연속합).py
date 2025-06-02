import sys

N = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().split()))

sub_sum = 0
result = 0

if all(x < 0 for x in nums):
    print(max(nums))

else:
    for c in range(N):
        sub_sum = max(0, sub_sum) + nums[c]
        result = max(sub_sum, result)

    print(result)
