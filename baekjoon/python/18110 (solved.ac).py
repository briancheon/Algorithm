import sys

def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(sys.stdin.readline().rstrip())

if n == 0:
    print(0)

else:
    opinions = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    opinions.sort()
    top_idx = n - roundUp(n * 0.15)
    bottom_idx = roundUp(n * 0.15)
    print(roundUp(sum(opinions[bottom_idx:top_idx]) / (top_idx - bottom_idx)))
