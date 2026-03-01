import sys

def star(n):
    if n == 1:
        return ["*"]
    
    if n == 2:
        return ["*****", "*    ", "* ***", "* * *", "* * *", "*   *", "*****"]

    parts = star(n - 1)
    result = ["*" * (4 * n - 3), "*" + " " * (4 * n - 4)]
    result.append("* " + parts[0] + "**")

    for i in range(1, len(parts)):
        result.append("* " + parts[i] + " *")

    result.extend(["*" + " " * (4 * n - 5) + "*", "*" * (4 * n - 3)])

    return result

N = int(sys.stdin.readline().rstrip())
answer = star(N)
if N != 1:
    answer[1] = answer[1].strip()
print("\n".join(answer))