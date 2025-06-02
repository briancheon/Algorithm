import sys

def josephus(n, k):
    nums = list(range(1, n + 1))
    jose = []
    index = 0
    for i in range(1, n + 1):
        index += k
        index %= len(nums)
        jose.append(nums.pop(index))

    return f"<{', '.join(map(str, jose))}>"

N, K = map(int, sys.stdin.readline().split())

print(josephus(N, K - 1))
