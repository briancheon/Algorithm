import sys

n = int(sys.stdin.readline().rstrip())
tiling = [0] * 1001
tiling[1] = 1
tiling[2] = 2

for i in range(3, n + 1):
    tiling[i] = tiling[i - 1] + tiling[i - 2]
        
print(tiling[n] % 10007)