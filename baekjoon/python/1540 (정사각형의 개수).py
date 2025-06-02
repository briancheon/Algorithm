import sys

N = int(sys.stdin.readline().rstrip())
biggest_square = int(N ** 0.5)

total_squares = 0

for i in range(1, biggest_square):
    total_squares += i * i

remainder = 0
for i in range(N - biggest_square ** 2, 0, -1):
    total_squares += remainder
    remainder = (remainder + 1) % biggest_square

print(total_squares)
