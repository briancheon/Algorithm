import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
next_index = 0

for i in range(N - 1):
    if nums[i] != nums[next_index]:
        next_index = i

    if nums[i] + 1 == nums[i + 1]:
        second_index = 0
        for j in range(i + 1, len(nums)):
            if nums[j] != nums[i + 1]:
                second_index = j
                break

        if not second_index:
            second_index = next_index
            next_index += 1

        nums[i + 1], nums[second_index] = nums[second_index], nums[i + 1]

print(*nums)
