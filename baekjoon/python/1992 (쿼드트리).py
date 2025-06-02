import sys

def pack(arr, n):
    check = sum(sum(row) for row in arr)
    if check == 0:
        return "0"
    
    elif check == n * n:
        return "1"
    
    result = "("
    for row_start in (0, n // 2):
        for col_start, col_end in ((0, n // 2), (n // 2, n)):
            temp = [arr[i][col_start:col_end] for i in range(row_start, row_start + n // 2)]
            result += pack(temp, n // 2)

    result += ")"

    return result

N = int(sys.stdin.readline().rstrip())
data = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

print(pack(data, N))