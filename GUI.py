# GUI Version of Sudoku Solver

from numpy import true_divide
import pygame
from solverV2 import solve, valid
import time
pygame.font.init()

class Grid:
    # Sudoku Board (zeroes are blanks)
    board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
             [6, 0, 0, 0, 7, 5, 0, 0, 9],
             [0, 0, 0, 6, 0, 1, 0, 7, 8],
             [0, 0, 7, 0, 4, 0, 2, 6, 0],
             [0, 0, 1, 0, 5, 0, 9, 3, 0],
             [9, 0, 4, 0, 6, 0, 0, 0, 5],
             [0, 7, 0, 3, 0, 0, 0, 1, 2],
             [1, 2, 0, 0, 0, 7, 4, 0, 0],
             [0, 4, 9, 2, 0, 6, 0, 0, 7]]

    # Constructor
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    # Function for updating the model
    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    # Function that sets the current selected spot (cube) to the given value
    def place(self, val):
        # get selected spot coords
        row, col = self.selected
        # Check that the current selected spot is "empty" (= 0)
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            # Check if value fits in the board at (row, col) and if it leads to a solution
            if valid(self.model, val, (row, col)) and solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    # Function for sketching in a given value to a selected spot (cube)
    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    # Function for drawing the board
    def draw(self, win):
        # Draw the Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i != 0 and i % 3 == 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0,0,0), (i*gap, 0), (i*gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)
    
    # Function for selecting a spot (cube)
    def select(self, row, col):
        # Reset current selected spot (cube)
        if self.selected:
            r, c = self.selected
            self.cubes[r][c].selected = False
        
        self.cubes[row][col].selected = True
        self.selected = (row, col)

    # Function for clearing a selected spot (cube) of sketched values
    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)
    
    # Function that gets the row and colum of the space that was clicked
    def click(self, pos):
        # Check if they clicked on the board
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.widht / 9
            x = pos[0] // gap
            y = pos[0] // gap
            return (int(y), int(x))
        else:
            return None
    
    # Function for checking if the board is solved/finished
    def is_finished(self):
        # Check for spot (cube) that has not been filled in
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False

        return True


# Cube (spot) class
class Cube:
    rows = 9
    cols = 9

    # Constructor
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
    
    # Function for drawing the cube
    def draw(self, win):
        # Blank cube (value = 0) will not be drawn and seen as blank

        # Get font
        fnt = pygame.font.SysFont("comicsans", 40)

        # Get coordinates
        gap = self.width / 9
        x = self.col * gap
        y = self.col * gap

        # Draw cube sketch
        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5,y+5))
        # Draw cube value
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0,0,0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height/2)))

        # Highlight cube if selected
        if self.selected:
            pygame.draw.rect(win, (0,255,0), (x,y,gap,gap), 3)

    # Function for setting the cube's value to a given value
    def set(self, val):
        self.value = val

    # Function for setting the cube's temp value (sketched value) to a given value
    def set(self, val):
        self.temp = val


# Function for redrawing the game window
def redraw_window(win, board, time, strikes):


# Main function
def main():
    
    