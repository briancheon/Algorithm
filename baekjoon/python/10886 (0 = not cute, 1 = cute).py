import sys

N = int(sys.stdin.readline().rstrip())

n_one = 0
n_zero = 0

for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        n_zero += 1
    else:
        n_one += 1
        
print("Junhee is cute!" if n_one > n_zero else "Junhee is not cute!")