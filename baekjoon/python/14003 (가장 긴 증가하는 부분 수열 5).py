import sys
from collections import deque


def bin_search(arr, x):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid - 1] < x < lis[mid]:
            return mid

        elif arr[mid] > x:
            end = mid - 1

        else:
            start = mid + 1

    return start


N = int(sys.stdin.readline().rstrip())
A = deque(map(int, sys.stdin.readline().split()))

lis = [float('-inf')]
lis_final = [(float('-inf'), 0)]

while A:
    n = A.popleft()

    if n > lis[-1]:
        lis_final.append((n, len(lis)))
        lis.append(n)

    else:
        idx = bin_search(lis, n)
        lis[idx] = n
        lis_final.append((n, idx))

lis_length = len(lis) - 1
lis = []

while lis_final and lis_length:
    num, idx = lis_final.pop()
    if idx == lis_length:
        lis.append(num)
        lis_length -= 1

print(len(lis))
print(*lis[::-1])