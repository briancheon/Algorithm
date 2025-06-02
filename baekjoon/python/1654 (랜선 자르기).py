import sys

K, N = map(int, sys.stdin.readline().split())

lines = [int(sys.stdin.readline().rstrip()) for _ in range(K)]
max_line = max(lines)

low, high = 1, max_line

while low <= high:
    mid = (low + high) // 2
    
    line_cnt = 0
    for line in lines:
        line_cnt += line // mid
    
    if line_cnt < N:
        high = mid - 1
    else:
        low = mid + 1
        
print(high)