import sys
from collections import deque

def bfs(board, s_r, s_c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    q = deque([(s_r, s_c, 1, 0)])
    visited = {(s_r, s_c, 1)}
    
    while q:
        r, c, target, moves = q.popleft()
        if target == 7:
            return moves
        
        for dy, dx in directions:
            nr, nc = r + dy, c + dx
            if 0 <= nr < 5 and 0 <= nc < 5 and board[nr][nc] != -1:
                new_target = target
                if board[nr][nc] == target:
                    new_target += 1

                if (nr, nc, new_target) not in visited:
                    visited.add((nr, nc, new_target))
                    q.append((nr, nc, new_target, moves + 1))

            skip_r, skip_c = r, c
            while True:
                next_r, next_c = skip_r + dy, skip_c + dx
                if not (0 <= next_r < 5 and 0 <= next_c < 5) or board[next_r][next_c] == -1:
                    break

                skip_r, skip_c = next_r, next_c

                if board[skip_r][skip_c] == 7:
                    break

            if skip_r != r or skip_c != c:
                new_target = target
                if board[skip_r][skip_c] == target:
                    new_target += 1

                if (skip_r, skip_c, new_target) not in visited:
                    visited.add((skip_r, skip_c, new_target))
                    q.append((skip_r, skip_c, new_target, moves + 1))
    
    return -1

board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

r, c = map(int, input().split())
print(bfs(board, r, c))