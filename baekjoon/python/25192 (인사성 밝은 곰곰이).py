import sys

N = int(sys.stdin.readline().rstrip())
_id = set()
count = 0

for _ in range(N):
    action = sys.stdin.readline().rstrip()
    if action == "ENTER":
        count += len(_id)
        _id = set()
    else:
        _id.add(action)

count += len(_id)
print(count)

