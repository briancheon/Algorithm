import math
M, N = int(input()), int(input())

answer = 0
for c in range(M, N + 1):
    if int(c ** 0.5) == c ** 0.5:
        answer += c

if answer != 0:
    print(answer)
    print(math.ceil(M ** 0.5) ** 2)
else:
    print(-1)
