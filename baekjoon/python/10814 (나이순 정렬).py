import sys

N = int(sys.stdin.readline().rstrip())

users = [list(sys.stdin.readline().split()) for i in range(N)]

users.sort(key=lambda x: int(x[0]))

for age, name in users:
    print(f'{age} {name}')
