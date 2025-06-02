import sys

while True:
    n, *heights = list(map(int, sys.stdin.readline().split()))

    if n == 0:
        break

    stack = []
    max_area = 0

    for i in range(n):
        j = i
        while stack and stack[-1][0] >= heights[i]:
            height, j = stack.pop()
            max_area = max(max_area, height * (i - j))
        stack.append((heights[i], j))

    while stack:
        height, j = stack.pop()
        max_area = max(max_area, height * (n - j))

    print(max_area)