import sys

N = int(sys.stdin.readline().rstrip())
X = list(map(int, sys.stdin.readline().split()))

X_set = sorted(list(set(X)))
X_index_dict = {X_set[_]: _ for _ in range(len(X_set))}

answer = map(lambda x: X_index_dict[x], X)
print(*answer, sep=' ')
