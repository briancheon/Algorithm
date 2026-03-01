import sys

N = int(sys.stdin.readline().rstrip())
count = 1
num = (N % 10) * 10 + (N // 10 + N % 10) % 10

while num != N:
    digit1, digit2 = num // 10, num % 10
    num = (num % 10) * 10 + (digit1 + digit2) % 10
    count += 1

print(count)


