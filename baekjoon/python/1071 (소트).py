import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))

num_count = [0] * 1111

for n in numbers:
    num_count[n] += 1

if len(list(set(numbers))) == 2:
    nums = list(set(numbers))
    if abs(nums[0] - nums[1]) == 1:
        print(*sorted(numbers, reverse=True), sep=' ')
    else:
        print(*sorted(numbers), sep=' ')

else:
    final = []
    cur = 0

    while sum(num_count) > 0:
        if num_count[cur]:
            if num_count[cur + 1]:
                for n in range(cur + 2, 1001):
                    if num_count[n]:
                        final.extend([cur] * num_count[cur])
                        final.append(n)
                        num_count[cur] = 0
                        num_count[n] -= 1
                        break
            else:
                final.extend([cur + 1] * num_count[cur + 1])
                final.extend([cur] * num_count[cur])
                num_count[cur] = 0
                num_count[cur + 1] = 0

        else:
            while final[cur]:
                final.append(cur)
                num_count[cur] -= 1

        cur += 1

    for num in final:
        print((str(num) + " "), end='')
