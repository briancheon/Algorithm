import sys

string = sys.stdin.readline().rstrip()
substring = set()

for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        substring.add(string[i:j])

print(len(substring))
