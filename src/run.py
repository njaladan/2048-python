"""
Clone of 2048 game.
"""

import random
import gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge_tiles(line):
    """
    This is a helper function
    to merge() that merges only 
    the tiles together.
    """
    
    merge_limit = [False for dummy_row in range(len(line))]
    check = 1 
    while check==1:
            
        line_check = line[0:]

        # for loop combines tiles (only once)
        for combine in range(0, len(line)-1):

            if (line[combine]==line[combine+1])&(line[combine]!=0)&(merge_limit[combine]!=1)&(merge_limit[combine+1]!=1):
                line[combine] = 2*line[combine]
                line[combine+1] = 0
                merge_limit[combine] = True
            if line_check == line:
                check = 0


def merge_zeros(line):
    """
    This is a helper function
    to merge() that only shifts 
    the zeros.
    """
    check = 1
    while check == 1:
        plus_zero = 0

        line_check = line[0:]
        # for loop shift zeros
        for lines in range(0, len(line)-1):

            if line[lines] == 0:
                plus_zero = 1

            if plus_zero == 1:
                line[lines] = line[lines+1]
                line[lines+1] = 0
        if line_check == line:
            check = 0




def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # just in case!
    if len(line)==1 or len(line)==0:
        return line

    # establish  variables for function
    check = 1

    # start while loop, necessary for not repeating infinitely

    print(line)
    super_check = 1
    while super_check == 1:

        super_line_check = line

        merge_zeros(line)
        
        merge_tiles(line)

        if super_line_check == line:
            super_check = 0
            
        check = 1

    while check == 1:
        plus_zero = 0

        line_check = line[0:]
        # for loop shift zeros
        for lines in range(0, len(line)-1):

            if line[lines] == 0:
                plus_zero = 1

            if plus_zero == 1:
                line[lines] = line[lines+1]
                line[lines+1] = 0
        if line_check == line:
            check = 0

        
    return line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Initialize an instance of the class.
        """

        # set all constants to the class
        self.grid_height = grid_height
        self.grid_width = grid_width

        # create the game grid
        self.grid = [[0 for dummy_row in range(self.grid_width)] for dummy_column in range(self.grid_height)]


    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # reinitialize the game grid
        self.grid = [[None for dummy_row in range(self.grid_width)] for dummy_column in range(self.grid_height)]



    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        # print the grid to the console
        for dummy_print in range(0,self.grid_height):
            print(self.grid[dummy_print])


    def get_grid_height(self):
        """
        Get the height of the grid.
        """

        # return the value grid_height

        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the grid.
        """
        # return the value grid_width

        return self.grid_width

    def move_left(self):
        """
        This is a helper function 
        that moves the tiles LEFT.
        """
        for row in range(0, self.grid_height):
            send_list = self.grid[row]
            new_row = merge(send_list)
            for dummy_tile in range(0, self.grid_width):
                self.set_tile(row, dummy_tile, new_row[dummy_tile])
                
        self.new_tile()
        
    def move_right(self):
        """
        This is a helper function 
        that moves the tiles RIGHT.
        """
        for row in range(0, self.grid_height):
            send_list = self.grid[row]
            send_list.reverse()
            new_row = merge(send_list)
            new_row.reverse()
            for dummy_tile in range(0, self.grid_width):
                self.set_tile(row, dummy_tile, new_row[dummy_tile])
                
        self.new_tile()
        
    def move_up(self):
        """
        This is a helper function 
        that moves the tiles UP.
        """
        for column in range(0, self.grid_width):
            send_list = []
            for tile in range(0, self.grid_height):
                send_list.append(self.grid[tile][column])
            new_row = merge(send_list)
            for dummy_set_tile in range(0, self.grid_height):
                self.set_tile(dummy_set_tile, column, new_row[dummy_set_tile])
                
        self.new_tile()
        
    def move_down(self):
        """
        This is a helper function 
        that moves the tiles DOWN.
        """
        for column in range(0, self.grid_width):
            send_list = []
            for tile in range(0, self.grid_height):
                send_list.append(self.grid[tile][column])
            send_list.reverse()
            new_row = merge(send_list)
            new_row.reverse()
            for dummy_set_tile in range(0, self.grid_height):
                self.set_tile(dummy_set_tile, column, new_row[dummy_set_tile])
                
        self.new_tile()
    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """

        # splits grid into strips, sends to merge()
        if direction == LEFT:
            self.move_left()
            
        elif direction == RIGHT:
            self.move_right()

        elif direction == UP:
            self.move_up()

        elif direction == DOWN:
            self.move_down()


    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        positions_with_zeros = []
        for row in range(self.grid_height):
           for col in range(self.grid_width):
               if self.grid[row][col] == 0:
                  zero_tile = [row, col]
                  positions_with_zeros.append(zero_tile)

        if len(positions_with_zeros) == 0:
            return None

        random_tile = random.choice(positions_with_zeros)

        new_tile_in_play = random.choice([2,2,2,2,2,2,2,2,4])

        self.set_tile(random_tile[0],random_tile[1], new_tile_in_play)


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # manually set the value to the list

        self.grid[row][col] = value


    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # one-liner - returns value from list

        return self.grid[row][col]


gui.run_gui(TwentyFortyEight(4, 4))
