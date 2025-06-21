import sys

def star(n):
    if n == 1:
        return ["*"]
    
    parts = star(n - 1)
    result = []
    if n % 2:
        result.append(" " * (2 ** n - 2) + "*" + " " * (2 ** n - 2))

        for i in range(2 ** n - 3, 2 ** (n - 1) - 1, -1):
            result.append(" " * i + "*" + " " * (2 ** (n + 1) - 3 - 2 * i - 2) + "*" + " " * i)

        for i in range(2 ** (n - 1) - 1, 0, -1):
            space = " " * ((2 ** (n + 1) - 3 - 2 * i - len(parts[2 ** (n - 1) - i - 1]) - 2) // 2)
            result.append(" " * i + "*" + space + parts[2 ** (n - 1) - i - 1] + space + "*" + " " * i)

        result.append("*" * (2 ** (n + 1) - 3))

    else:
        result.append("*" * (2 ** (n + 1) - 3))

        for i in range(1, 2 ** (n - 1)):
            space = " " * ((2 ** (n + 1) - 3 - 2 * i - len(parts[i - 1]) - 2) // 2)
            result.append(" " * i + "*" + space + parts[i - 1] + space + "*" + " " * i)

        for i in range(2 ** (n - 1), 2 ** n - 2):
            result.append(" " * i + "*" + " " * (2 ** (n + 1) - 3 - 2 * i - 2) + "*" + " " * i)

        result.append(" " * (2 ** n - 2) + "*" + " " * (2 ** n - 2))

    return result

N = int(sys.stdin.readline().rstrip())
print('\n'.join(map(lambda x: x.rstrip(), star(N))))