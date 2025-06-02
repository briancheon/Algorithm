import sys

N = int(sys.stdin.readline().rstrip())
heights = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

stack = []
max_area = 0

for i in range(N):
    j = i
    while stack and stack[-1][0] >= heights[i]:
        height, j = stack.pop()
        max_area = max(max_area, height * (i - j))
    stack.append((heights[i], j))

while stack:
    height, j = stack.pop()
    max_area = max(max_area, height * (N - j))

print(max_area)