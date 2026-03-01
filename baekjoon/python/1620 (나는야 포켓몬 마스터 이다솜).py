import sys

N, M = map(int, sys.stdin.readline().split())

no_name, name_no = {}, {}

for c in range(N):
    pokemon = sys.stdin.readline().rstrip()
    no_name[c + 1] = pokemon
    name_no[pokemon] = c + 1

for c in range(M):
    quiz = sys.stdin.readline().rstrip()
    try:
        int(quiz)
    except ValueError:
        print(name_no[quiz])
    else:
        print(no_name[int(quiz)])
