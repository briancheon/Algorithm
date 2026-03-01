import sys
from functools import reduce

def calc_xor(n):
    if n % 4 == 0:
        return n

    elif n % 4 == 1:
        return 1

    elif n % 4 == 2:
        return n + 1

    elif n % 4 == 3:
        return 0
    
def xor_range(l, r):
    return calc_xor(l - 1) ^ calc_xor(r)
    

N = int(sys.stdin.readline().rstrip())
dump_trucks = [xor_range(X, X + M - 1) for _ in range(N) for X, M in [map(int, sys.stdin.readline().split())]]

nim_sum = reduce(lambda x, y: x ^ y, dump_trucks)

print("koosaga" if nim_sum else "cubelover")