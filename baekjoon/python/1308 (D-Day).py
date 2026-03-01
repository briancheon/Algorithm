import sys
import datetime

today = datetime.date(*map(int, sys.stdin.readline().split()))
dday = datetime.date(*map(int, sys.stdin.readline().split()))

days_left = (dday - today).days
check = (dday.year - today.year > 1000) or \
        (dday.year - today.year == 1000 and  today.month <= dday.month and today.day <= dday.day)

print("gg" if check else f'D-{days_left}')