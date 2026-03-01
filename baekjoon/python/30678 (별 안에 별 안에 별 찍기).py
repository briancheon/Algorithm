import sys

def star_in_star(n):
    if n == 0:
        return ["*"]
    
    parts = star_in_star(n - 1)
    spaces = " " * (5 ** (n - 1))
    result = []

    for _ in range(2):
        for part in parts:
            result.append(spaces * 2 + part + spaces * 2)
        
    for part in parts:
        result.append(part * 5)

    for part in parts:
        result.append(spaces + part * 3 + spaces)
    
    for part in parts:
        result.append((spaces + part) * 2 + spaces)

    return result
    
N = int(sys.stdin.readline().rstrip())

print(*star_in_star(N), sep='\n')