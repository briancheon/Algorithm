import sys

N, M = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
max_square = 0

for i in range(N):
    for j in range(M):
        for k in range(N - i):
            for l in range(M - j):
                check = ""
                for m in range(min(N // k + 1, M // l + 1)):
                    check += arr[i + k * m][j + l * m]
                    if int(int(check) ** 0.5) ** 2 == int(check):
                        if int(check) > max_square:
                            max_square = int(check)

                    elif int(int(check[::-1]) ** 0.5) ** 2 == int(check[::-1]):
                        if int(check[::-1]) > max_square:
                            max_square = int(check[::-1])

print(max_square)
