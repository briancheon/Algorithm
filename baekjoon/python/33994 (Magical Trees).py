import sys

N = int(sys.stdin.readline().rstrip())

if N % 2 == 0:
    print("No")
    
else:
    print("Yes")
    for i in range(1, N):
        print(i, i + 1)

    for i in range(1, N - 1, 2):
        print(i, i + 1)
        print(i, i + 2)

    for i in range(1, N - 1, 2):
        print(i, i + 2)
        print(i + 1, i + 2)