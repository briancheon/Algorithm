import sys

min, max = map(int, sys.stdin.readline().split())
count = max - min + 1

is_square_divisible = [False] * count

for i in range(2, int(max ** 0.5) + 1):
    square = i ** 2
    for j in range(((min - 1) // square + 1) * square, max + 1, square):
        if not is_square_divisible[j - min]:
            is_square_divisible[j - min] = True
            count -= 1
    
print(count)