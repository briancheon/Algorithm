import sys

def longest_consecutive(arr):
    if not arr:
        return 0

    longest_streak = 1
    current_streak = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_streak += 1
        
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1

    return max(longest_streak, current_streak)

N = int(sys.stdin.readline().rstrip())
B = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
items = list(set(B))

maximum = 0

for i in range(len(items)):
    check = list(filter(lambda x: x != items[i], B))
    maximum = max(maximum, longest_consecutive(check))

print(maximum)