import sys

def valid(s):
    q = []
    for c in s:
        if c == "(":
            q.append("(")
        elif c == "[":
            q.append("[")
        elif c == ")":
            if q and q[-1] == "(":
                q.pop()
            else:
                q.append(")")
                break
        elif c == "]":
            if q and q[-1] == "[":
                q.pop()
            else:
                q.append("]")
                break

    return "no" if q else "yes"

while True:
    string = sys.stdin.readline().rstrip()
    if string == ".":
        break
    else:
        print(valid(string))
