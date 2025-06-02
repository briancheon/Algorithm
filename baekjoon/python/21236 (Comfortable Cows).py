import sys

N = int(sys.stdin.readline().rstrip())
pasture = [[0] * 1000] * 1000

count = 0

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    
    