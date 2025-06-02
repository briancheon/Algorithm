import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

stack = []

operations = []
possible = True

cur = 1

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    
    while cur <= num:
        stack.append(cur)
        operations.append("+")
        cur += 1
        
    if stack[-1] == num:
        stack.pop()
        operations.append("-")
        
    else:
        possible = False
        break
    
if possible:
    print(*operations, sep='\n')

else:
    print("NO")