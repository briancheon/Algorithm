import sys

def maxSubArray(nums):
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
            
    return max_global

input = sys.stdin.read
data = input().split()
N = int(data[0])
nums = list(map(int, data[1:N+1]))
sys.stdout.write(str(maxSubArray(nums)) + '\n')