import sys

eq = sys.stdin.readline().rstrip()
answer, temp, num = 0, 0, ""

for s in eq:
    if s.isnumeric():
        num += s
    elif s == "+":
        temp += int(num)

