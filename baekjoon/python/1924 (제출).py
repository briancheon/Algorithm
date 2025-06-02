import sys

num_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days = {0: "MON", 1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN"}

x, y = map(int, sys.stdin.readline().split())

past_days = y - 1
for i in range(1, x):
    past_days += num_days[i]

print(days[past_days % 7])
