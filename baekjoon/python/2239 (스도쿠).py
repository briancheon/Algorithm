import sys

def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def sudoku(grid, row, col):
    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return sudoku(grid, row, col + 1)

    for num in range(1, 10, 1):
        if solve(grid, row, col, num):
            grid[row][col] = num
            if sudoku(grid, row, col + 1):
                return True

        grid[row][col] = 0
    return False

grid = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(9)]

sudoku(grid, 0, 0)

for row in grid:
    print(''.join(map(str, row)))