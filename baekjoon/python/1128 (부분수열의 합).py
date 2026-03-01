import sys

def backtrack(arr, idx, cur_sum, target, cnt):
	if idx == len(arr):
		if cur_sum == target:
			return cnt + 1
		return cnt

	cnt += backtrack(arr, idx + 1, cur_sum + arr[idx], target, cnt) + backtrack(arr, idx + 1, cur_sum, target, cnt) 
	
	return cnt
	
N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

answer = backtrack(nums, 0, 0, S, 0)

print(answer if S else answer - 1)