
import sys
R, C = map(int, sys.stdin.readline().split())
data = [sys.stdin.readline().rstrip() for _ in range(R)]

max_perimeter = 0
hist = [0] * C

for i in range(R):
    for j in range(C):
        if data[i][j] == '.':
            hist[j] += 1
        else:
            hist[j] = 0

    stack = []
    for j in range(C + 1):
        current_height = 0 if j == C else hist[j]
        while stack and current_height < hist[stack[-1]]:
            h = hist[stack.pop()]
            width = j if not stack else j - stack[-1] - 1
            perimeter = 2 * (h + width)
            if perimeter > max_perimeter:
                max_perimeter = perimeter
        stack.append(j)

print(max_perimeter - 1)
