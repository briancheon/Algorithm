import sys

string = sys.stdin.readline().rstrip()

s = ''
for i in range(len(string)):
    if i % 10 == 0 and i != 0:
        print(s)
        s = ''
    s += string[i]
    
print(s)