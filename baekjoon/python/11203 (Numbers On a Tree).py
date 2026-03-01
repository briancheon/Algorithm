import sys
        
data = sys.stdin.readline().split()
string = ""
if len(data) == 1:
    N = int(data[0])

else:
    N, string = data
    N = int(N)

cur = 1
for s in string:
    if s == "L":
        cur = 2 * cur

    else:
        cur = 2 * cur + 1

print(2 ** (N + 1) - cur)