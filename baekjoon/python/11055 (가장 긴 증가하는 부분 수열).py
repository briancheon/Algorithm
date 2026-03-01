import sys

A = int(sys.stdin.readline().rstrip())
A_ls = list(map(int, sys.stdin.readline().split()))

sums = [0] * A

for i in range(A):
    sums[i] = A_ls[i]
    for j in range(i):
        if A_ls[j] < A_ls[i]:
            sums[i] = max(sums[i], sums[j] + A_ls[i])
            
print(max(sums))