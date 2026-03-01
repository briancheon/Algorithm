import sys

N = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

left, right = 3, N
answer = 2

while left <= right:
    mid = (left + right) // 2
    
    need = [0] * (mid + 2)

    for i in range(N):
        if a[i] >= mid or a[i] <= 1:
            need[0] += 1

        else:
            need[a[i]] += 1

    x = 1
    for i in range(mid - 1, 1, -1):
        if need[i] >= x:
            need[0] += need[i] - x
            continue
        
        x += x - need[i]
        if x > N:
            break

    if need[0] >= 2 * x:
        answer = max(mid, answer)
        left = mid + 1
        continue
    
    right = mid - 1

print(answer)