import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    conditions = {condition: int(time) for data in sys.stdin.readline().rstrip().split(",") 
                  for condition, time in [data.split(":")]}
    min_time = min(max(conditions[condition] for condition in data.split("&")) 
                   for data in sys.stdin.readline().rstrip().split("|"))

    print(min_time)