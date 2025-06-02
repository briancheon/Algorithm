import sys

N, M = map(int, sys.stdin.readline().split())

password_dict = {}

for _ in range(N):
    address, password = sys.stdin.readline().split()
    password_dict[address] = password
    
for _ in range(M):
    address = sys.stdin.readline().rstrip()
    print(password_dict[address])