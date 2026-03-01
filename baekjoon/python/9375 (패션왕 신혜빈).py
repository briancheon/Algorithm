import sys

def ls_product(arr):
    result = 1
    for i in arr:
        result *= (i + 1)

    return result

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    clothings = {}
    for _ in range(n):
        _, c_type = sys.stdin.readline().split()
        clothings[c_type] = clothings.get(c_type, 0) + 1

    n_clothings = clothings.values()
    print(ls_product(n_clothings) - 1)