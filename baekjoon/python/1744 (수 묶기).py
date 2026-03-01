import sys

N = int(sys.stdin.readline().rstrip())
pos_nums, neg_nums = [], []

for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n > 0:
        pos_nums.append(n)
    else:
        neg_nums.append(n)

total = 0

pos_nums.sort(reverse=True)
neg_nums.sort()

if len(pos_nums):
    for c in range(1, len(pos_nums), 2):
        if pos_nums[c] > 1 and pos_nums[c - 1] > 1:
            total += pos_nums[c] * pos_nums[c - 1]
        else:
            total += pos_nums[c] + pos_nums[c - 1]


    total += pos_nums[-1] if len(pos_nums) % 2 else 0

if len(neg_nums):
    for c in range(1, len(neg_nums), 2):
        total += neg_nums[c] * neg_nums[c - 1]

    total += neg_nums[-1] if len(neg_nums) % 2 else 0

print(total)