# Second version of Sudoku Solver program

# Board variable (zeroes represent blanks)
board = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

# Main function
def solve(bo):
    # Find empty spot in given board
    find = find_empty(bo)
    
    # If there is no empty spot
    if not find:
        return True
    # If there is an empty spot
    else:
        row, col = find
    
    for i in range(1, 10):
        # Figure out if i fits in the board at (row, col)
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            
            # Recursively call solve
            if solve(bo):
                return True
            
            # Reset value if value does not work
            bo[row][col] = 0
    
    return False

# Function for checking if the current board is valid
def valid(bo, num, pos):
    # Check if num is in the given row (pos[0]) -
    for i in range(len(bo[0])):
        if pos[1] != i and bo[pos[0]][i] == num:
            return False

    # Check if num is in the given column (pos[1]) -
    for i in range(len(bo)):
        if pos[0] != i and bo[i][pos[1]] == num:
            return False
    
    # Check if num is in the current square -
    box_x = pos[1] // 3 # get which of the three horizontal boxes that we are in
    box_y = pos[0] // 3 # get which of the three vertical boxes that we are in
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if (i, j) != pos and bo[i][j] == num:
                return False

    # Did NOT find num in the given row, column, and square/box
    return True

# Function for printing the board
def print_board(bo):
    print("")

    for i  in range(len(bo)):
        # At the start of every 3rd section, print a line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        
        # print values in row i
        for j in range(len(bo[0])):
            # prints separator line after every 3rd column
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            # prints the last value in row i
            if j == 8:
                print(bo[i][j])
            # prints all other values 
            else:
                print(str(bo[i][j]) + " ", end="")

    print("")

# print_board(board)

# Function for finding the next empty spot in a given board
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # (row, col) or (y, x)

    return None

print_board(board)
solve(board)
print_board(board)