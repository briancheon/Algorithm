import sys

N = int(sys.stdin.readline().rstrip())

flowers = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
flowers.sort()

i = 0
last_day = (3, 1)
cnt = 0

while i < N:
    s_mon, s_day, e_mon, e_day = flowers[i]
    if (s_mon, s_day) <= last_day < (e_mon, e_day):
        max_day = (e_mon, e_day)
        while i < N - 1:
            temp_s_mon, temp_s_day, temp_e_mon, temp_e_day = flowers[i + 1]
            if last_day < (temp_s_mon, temp_s_day):
                break
            if max_day < (temp_e_mon, temp_e_day):
                max_day = (temp_e_mon, temp_e_day)
            i += 1
    
        last_day = max_day
        cnt += 1
    
        if last_day > (11, 30):
            break
    i += 1

if last_day > (11, 30):
    print(cnt)
else:
    print(0)