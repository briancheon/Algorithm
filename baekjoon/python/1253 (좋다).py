import sys

N = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

good = 0

for c in range(N):
    p1 = 0
    p2 = N - 1
    target = nums[c]

    while p1 < p2:
        check = nums[p1] + nums[p2]

        if check == target:
            if p1 != c and p2 != c:
                good += 1
                break
            elif p1 == c:
                p1 += 1
            else:
                p2 -= 1

        elif check < target:
            p1 += 1
        else:
            p2 -= 1

print(good)
