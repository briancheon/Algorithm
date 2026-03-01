import sys

def binary_search(arr, x):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        
        if arr[mid] < x:
            start = mid + 1

        else:
            end = mid - 1

    return start


N, Q = map(int, sys.stdin.readline().split())

menu = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
menu.sort()

spicy, sweet = map(list, zip(*menu))
ranges = []

for _ in range(Q):
    u, v, x, y = map(int, sys.stdin.readline().split())
    left, right = binary_search(spicy, u), binary_search(spicy, v + 1)

    sweet_check = sorted(sweet[left:right])
    left, right = binary_search(sweet_check, x), binary_search(sweet_check, y + 1)
    print(right - left)