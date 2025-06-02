import sys

N, jimin, hansoo = map(int, sys.stdin.readline().split())
count = 0

while jimin != hansoo:
    jimin -= jimin // 2
    hansoo -= hansoo // 2
    count += 1

print(count)
