import sys
import math

K = int(sys.stdin.readline().rstrip())
four_seven = ""

while K:
    n = int(math.log(K + 1, 2))
    
    if K - 2 ** n + 1 <= (2 ** n - 1) // 2:
        four_seven += "4"
        K -= 2 ** (n - 1)
    else:
        four_seven += "7"
        K -= 2 ** n
    
print(four_seven)
    
    