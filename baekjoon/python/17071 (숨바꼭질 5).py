import sys

N, K = map(int, sys.stdin.readline().split())

if N == K:
    print(0)
    sys.exit()

visited = [[False] * 500001 for _ in range(2)]
parent = [[-1] * 500001 for _ in range(2)]

visited[0][N] = True
current_positions = [N]
time = 0

while True:
    time += 1
    target = K + time * (time + 1) // 2
    if target > 500000:
        break

    curr_parity = time % 2
    next_positions = []

    visited[curr_parity] = [False] * 500001
    parent[curr_parity] = [-1] * 500001

    for pos in current_positions:
        for nxt in (pos - 1, pos + 1, pos * 2):
            if 0 <= nxt <= 500000 and not visited[curr_parity][nxt]:
                visited[curr_parity][nxt] = True
                parent[curr_parity][nxt] = pos
                next_positions.append(nxt)

    if visited[curr_parity][target]:
        result_time = time
        cur = target
        cur_parity = curr_parity
        t = time
        while t > 0:
            cur = parent[cur_parity][cur]
            t -= 1
            cur_parity = t % 2

        print(result_time)
        sys.exit()

    if not next_positions:
        break

    current_positions = next_positions

print(-1)
