import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

if N <= 1:
    print("A")

elif N == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    
    else:
        print("A")

else:
    candidates = [(a, arr[1] - arr[0] * a) for a in range(-200, 201)]
    possible = False

    for a, b in candidates:
        if all(arr[i] == a * arr[i - 1] + b for i in range(1, N)):
            print(a, b)
            possible = True
            break

    print(a * arr[N - 1] + b if possible else "B")
