import sys

T = int(sys.stdin.readline().rstrip())

answers = [0, 1, 2, 4] + [0] * 8

for i in range(4, 12):
    answers[i] = answers[i - 3] + answers[i - 2] + answers[i - 1]

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    
    print(answers[n])