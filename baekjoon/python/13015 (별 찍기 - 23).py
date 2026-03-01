import sys

N = int(sys.stdin.readline().rstrip())

print("*" * N + " " * (2 * N - 3) + "*" * N)

for i in range(N - 2):
    print(" " * (i + 1) + "*" + " " * (N - 2) + "*" + " " * (2 * N - 3 - 2 * (i + 1)) + "*" + " " * (N - 2) + "*")

print(" " * (N - 1) + ("*" + " " * (N - 2)) * 2 + "*")

for i in range(N - 3, -1, -1):
    print(" " * (i + 1) + "*" + " " * (N - 2) + "*" + " " * (2 * N - 3 - 2 * (i + 1)) + "*" + " " * (N - 2) + "*")

print("*" * N + " " * (2 * N - 3) + "*" * N)