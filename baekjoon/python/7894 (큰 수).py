import sys
import math

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    m = int(sys.stdin.readline().rstrip())
    
    if m == 1:
        print(1)
        continue
    
    log_fact = sum(map(lambda x: math.log10(x), range(1, m + 1)))
    
    print(math.ceil(log_fact))