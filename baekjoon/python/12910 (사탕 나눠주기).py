import sys

N = int(sys.stdin.readline())
candies = sorted(list(map(int, sys.stdin.readline().split())))

if candies[0] != 1:
    print(0)

else:
    result, m = 0, 1
    for c in range(1, candies[-1] + 1):
        if c not in candies:
            break
        m *= candies.count(c)
        result += m
    print(result)
