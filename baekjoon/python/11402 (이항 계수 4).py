import sys
import math

N, K, M = map(int, sys.stdin.readline().split())

ls_N, ls_K = [], []
answer = 1

while N != 0:
    ls_N.append(N % M)
    ls_K.append(K % M)
    
    N, K = N // M, K // M
    
for i in range(len(ls_N)):
    answer *= math.comb(ls_N[i], ls_K[i])

print(answer % M)