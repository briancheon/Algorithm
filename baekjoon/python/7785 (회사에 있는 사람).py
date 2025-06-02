import sys

n = int(sys.stdin.readline().rstrip())

people = {}

for c in range(n):
    name, state = sys.stdin.readline().split()
    if state == "enter":
        people[name] = True
    else:
        people[name] = False

current = sorted(list(filter(lambda x: people[x], people)))[::-1]
for person in current:
    print(person)
