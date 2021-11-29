#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-11-15
Purpose: Rock the Casbah
"""


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    input_sudoku = [[0, 0, 0, 0, 5, 2, 0, 4, 0],
                    [0, 0, 3, 6, 7, 0, 0, 0, 9],
                    [0, 6, 0, 0, 0, 3, 5, 0, 0],
                    [0, 9, 0, 0, 2, 6, 8, 0, 0],
                    [0, 0, 0, 0, 0, 7, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 2, 0],
                    [1, 3, 0, 0, 0, 8, 0, 0, 0],
                    [0, 0, 4, 1, 0, 5, 0, 0, 0],
                    [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    # 0 means the cells where no value is assigned
    print('Input Sudoku:')
    print_table(input_sudoku)
    print('\n--------------------------------------\n')
    if Sudoku(input_sudoku, 0, 0):
        print('Here is the solver:')
        print_table(input_sudoku)
    else:
        print("Something is wrong. Please check your sudoku again!!!")


# --------------------------------------------------
def puzzle(a):
    """Find cell to fill"""

    M = 9
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


# --------------------------------------------------
def solve(grid, row, col, num):
    """Algorithm for solving sudoku"""

    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


# --------------------------------------------------
def Sudoku(grid, row, col):
    """Make row and column for sudoku"""

    M = 9
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Sudoku(grid, row, col + 1)
    for num in range(1, M + 1, 1):
        if solve(grid, row, col, num):
            grid[row][col] = num
            if Sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


# --------------------------------------------------
def print_table(bo):
    """Create and print the table"""

    for i in range(len(bo)):
        if i % 3 == 0:
            if i == 0:
                print(" ┎─────────────────────────────┒")
            else:
                print(" ┠─────────────────────────────┨")

        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" ┃ ", end=" ")

            if j == 8:
                print(bo[i][j], " ┃")
            else:
                print(bo[i][j], end=" ")

    print(" ┖─────────────────────────────┚")


# --------------------------------------------------
if __name__ == '__main__':
    main()
