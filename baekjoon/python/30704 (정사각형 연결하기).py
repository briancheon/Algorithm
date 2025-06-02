import sys
import math

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    side1 = int(N ** 0.5)
    side2 = math.ceil(N / side1)
    
    
    print(2 * (side1 + side2))
    