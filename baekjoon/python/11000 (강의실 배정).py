"""import sys

def num_rooms(ls):
    num_room = 1
    cur = ls.pop(0)
    ls2 = []
    while ls or ls2:
        for room in ls:
            if room[0] < cur[1]:
                ls2.append(room)
            else:
                cur = room
        if len(ls2) == 0:
            break
        num_room += 1
        ls = []
        cur = ls2.pop(0)
        for room in ls2:
            if room[0] < cur[1]:
                ls.append(room)
            else:
                cur = room
        if len(ls) == 0:
            break
        num_room += 1
        ls2 = []
        cur = ls.pop(0)
    return num_room

N = int(sys.stdin.readline().rstrip())

times = []

for c in range(N):
    time = tuple(map(int, sys.stdin.readline().split()))
    times.append(time)

times.sort()
print(num_rooms(times))"""

# Using Heap
import sys
import heapq

def num_rooms(ls):
    end_times = []
    heapq.heappush(end_times, ls[0][1])
    for i in range(1, len(ls)):
        if ls[i][0] >= end_times[0]:
            heapq.heappop(end_times)
        heapq.heappush(end_times, ls[i][1])
    return len(end_times)

N = int(sys.stdin.readline().rstrip())

times = []

for c in range(N):
    time = tuple(map(int, sys.stdin.readline().split()))
    times.append(time)

times.sort()
print(num_rooms(times))
