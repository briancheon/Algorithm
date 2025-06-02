import sys

H, W = map(int, sys.stdin.readline().split())
data = []
for i in range(H):
    data.append(sys.stdin.readline().rstrip())

answer = []
for i in range(H):
    row = []
    cloud = False
    num = -1
    for j in range(W):
        if data[i][j] == "c":
            num = 0
            cloud = True
        elif cloud:
            num += 1
        row.append(num)
    answer.append(row)

for i in range(H):
    print(*answer[i])
