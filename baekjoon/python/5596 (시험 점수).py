import sys

mingook = sum(map(int, sys.stdin.readline().split()))
mansae = sum(map(int, sys.stdin.readline().split()))

if mingook >= mansae:
    print(mingook)
else:
    print(mansae)
