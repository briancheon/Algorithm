import sys

X = int(sys.stdin.readline().rstrip())

sticks = [64]

while sum(sticks) != X:
    if sum(sticks) > X:
        smallest_stick = sticks.pop()
        sticks.append(smallest_stick >> 1)
        if sum(sticks) < X:
            sticks.append(smallest_stick >> 1)
            
print(len(sticks))
        


