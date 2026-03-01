import sys

def num_papers(arr, n, w_cnt, b_cnt):
    check = sum(sum(row) for row in arr)
    if check == 0:
        return w_cnt + 1, b_cnt
    
    elif check == n * n:
        return w_cnt, b_cnt + 1
    
    for row_start in (0, n // 2):
        for col_start, col_end in ((0, n // 2), (n // 2, n)):
            temp = [arr[i][col_start:col_end] for i in range(row_start, row_start + n // 2)]
            w_cnt, b_cnt = num_papers(temp, n // 2, w_cnt, b_cnt)

    return w_cnt, b_cnt

N = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white, blue = num_papers(paper, N, 0, 0)
print(white)
print(blue)