import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

Q = int(sys.stdin.readline().rstrip())
w = list(map(int, sys.stdin.readline().split()))

gaps = [A[i] - B[i] for i in range(N)]

def calculate_scores(gaps, birds):
    birds = sorted(set(birds), reverse=True)
    scores = {}
    cur = 0
    score = 0

    for gap in gaps:
        while cur < len(birds) and birds[cur] > gap:
            scores[birds[cur]] = score
            cur += 1
        score += 1

    while cur < len(birds):
        scores[birds[cur]] = score
        cur += 1

    return scores

scores = calculate_scores(gaps, w)

for bird in w:
    print(scores[bird])