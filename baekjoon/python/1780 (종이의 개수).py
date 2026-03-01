import sys

def num_paper(arr, n, cnt_1, cnt0, cnt1):
    check = arr[0][0]
    one_paper = all(arr[i][j] == check for i in range(n) for j in range(n))
    if check == 0 and one_paper:
        return cnt_1, cnt0 + 1, cnt1
    
    elif check == 1 and one_paper:
        return cnt_1, cnt0, cnt1 + 1
    
    elif check == -1 and one_paper:
        return cnt_1 + 1, cnt0, cnt1

    for i in range(3):
        for j in range(3):
            temp = [row[(n // 3) * j:(n // 3) * (j + 1)] for row in arr[(n // 3) * i:(n // 3) * (i + 1)]]
            cnt_1, cnt0, cnt1 = num_paper(temp, n // 3, cnt_1, cnt0, cnt1)
    
    return cnt_1, cnt0, cnt1

N = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(*num_paper(paper, N, 0, 0, 0), sep='\n')