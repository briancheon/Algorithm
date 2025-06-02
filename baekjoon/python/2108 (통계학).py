import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
nums = defaultdict(int)
numbers = []
total = 0


for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    numbers.append(n)
    nums[n] += 1
    total += n

numbers.sort()
modes = sorted(nums.items(), key=lambda x: (x[1], -x[0]), reverse=True)

average = round(total / N)
median = numbers[N // 2]
if len(modes) == 1 or modes[0][1] != modes[1][1]:
    mode = modes[0][0]
else:
    mode = modes[1][0]
range = numbers[-1] - numbers[0]

print(average)
print(median)
print(mode)
print(range)
