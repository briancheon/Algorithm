import sys

def triangle(a, b, c):
    l = list(sorted([a, b, c]))
    if l[2] >= l[0] + l[1]:
        return "Invalid"
    else:
        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or c == a:
            return "Isosceles"
        else:
            return "Scalene"

l1, l2, l3 = map(int, sys.stdin.readline().split())
while l1 + l2 + l3 != 0:
    print(triangle(l1, l2, l3))
    l1, l2, l3 = map(int, sys.stdin.readline().split())
