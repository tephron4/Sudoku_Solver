import numpy as np

# zeroes represent blanks, 
#   because sudoku numbers are on an interval of [1,9]
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

# print the grid
print(np.matrix(grid))

# Function that finds out if a number already exists
#   in the given row, column, or square
def possible(row, col, num):
    global grid # allows us to use the grid variable that is defined outside of the function

    # Check if the number is in the given row - 
    for i in range(0,9):
        if grid[row][i] == num:
            return False
    # Check if the number is in the given column -
    for i in range(0,9):
        if grid[i][col] == num:
            return False
    # Check if the number is in the given square -
    x0 = (col // 3) * 3 # starting column of the given square
    y0 = (row // 3) * 3 # starting row of the given square
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == num:
                return False

    # Did not find that number in any of the given row, column, or square
    return True

# Function that solves a sudoku puzzle
def solve():
    global grid # allows us to use the grid variable that is defined outside of the function
    
    for row in range(0,9):
        for col in range(0,9):
            # Check for blank space -
            if grid[row][col] == 0:
                for num in range(1,10):
                    if possible(row,col,num):
                        grid[row][col] = num
                        solve()
                        grid[row][col] = 0
                return
    
    print(np.matrix(grid))
    input('More possible solutions')

solve()

