import sys
import bisect

N = int(sys.stdin.readline().rstrip())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A_dict = {a: i for i, a in enumerate(A)}
B_dict = {b: i for i, b in enumerate(B)}

arr = [B_dict[A[i]] for i in range(N)]

lcs = []
for i in range(N):
    if not lcs:
        lcs.append(arr[i])
    
    elif arr[i] > lcs[-1]:
        lcs.append(arr[i])
    
    else:
        idx = bisect.bisect_left(lcs, arr[i])
        lcs[idx] = arr[i]
        
print(len(lcs))