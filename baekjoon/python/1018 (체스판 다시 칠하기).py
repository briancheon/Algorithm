import sys

chessboard = ["BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB",
              "WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW"]

def square_count(matrix):
    c1, c2 = 0, 0
    for i in range(64):
        if matrix[i] != chessboard[0][i]:
            c1 += 1
        if matrix[i] != chessboard[1][i]:
            c2 += 1
    return min(c1, c2)

N, M = map(int, sys.stdin.readline().split())
chess = []
for _ in range(N):
    chess.append(''.join(sys.stdin.readline().split()))

minimum = float('inf')

for a in range(N - 7):
    for b in range(M - 7):
        test = ""
        for c in range(8):
            test += chess[a + c][b:b+8]

        count = square_count(test)
        if count < minimum:
            minimum = count

print(minimum)

