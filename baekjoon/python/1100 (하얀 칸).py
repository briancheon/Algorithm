import sys

board = []

for c in range(8):
    board.extend(sys.stdin.readline().split())

count = 0
for i in range(8):
    if i % 2 == 0:
        for j in range(0, 8, 2):
            if board[i][j] == 'F':
                count += 1
    else:
        for j in range(1, 8, 2):
            if board[i][j] == 'F':
                count += 1

print(count)

