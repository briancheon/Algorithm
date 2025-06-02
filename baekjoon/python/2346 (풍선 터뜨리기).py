import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
balloons = deque(enumerate(map(int, sys.stdin.readline().split()), 1))

num, index = balloons.popleft()
print(num, end=' ')

for i in range(N - 1):
    balloons.rotate((-index + 1, -index)[index < 0])
    num, index = balloons.popleft()
    print(num, end=' ')
