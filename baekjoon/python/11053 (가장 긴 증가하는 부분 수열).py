import sys

A = int(sys.stdin.readline().rstrip())
A_ls = list(map(int, sys.stdin.readline().split()))

length = [0] * A

for i in range(A):
    length[i] = 1
    for j in range(i):
        if A_ls[j] < A_ls[i]:
            length[i] = max(length[i], length[j] + 1)
            
print(max(length))