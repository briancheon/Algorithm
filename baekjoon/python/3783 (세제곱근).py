import sys
from decimal import Decimal, getcontext, ROUND_DOWN

getcontext().prec = 1000

T = int(sys.stdin.readline().rstrip())

for c in range(T):
    n = Decimal(sys.stdin.readline().rstrip())
    power = Decimal('1') / Decimal('3')
    
    decimal_n = Decimal(n ** power)
    decimal_n = round(decimal_n, 100)
    
    decimal_n = Decimal(decimal_n).quantize(Decimal('.0000000000'), rounding=ROUND_DOWN)
    
    print(decimal_n)
    

