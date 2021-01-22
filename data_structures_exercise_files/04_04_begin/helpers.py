"""
Python Data Structures and Algorithms - A Game-Based Approach
Helper functions and values for use with other files in this project.
Robin Andrews - https://compucademy.net/
"""

# i, j, row, col

offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


def read_maze(file_name):
    """
    Reads a maze stored in a text file and returns a 2d list containing the maze representation.
    """
    try:
        with open(file_name, "r", newline=None) as fh:
            maze = [[char for char in line.strip("\r\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular.")
                    raise SystemExit
            return maze
    except IOError:
        print("There is a problem with the file you have selected.")
        raise SystemExit


def is_legal_pos(maze, pos):
    i, j = pos

    # number of elements in a 2d array are the number objects in it
    # stacked on top of each other
    num_rows = len(maze)
    # counting the len of the first item row ti gwt how many columns
    num_cols = len(maze[0])
    # return True if the following statement works
    # i is larger than 0 and less than the number of rows
    # j is is larger or equal to the number of columns
    # coordinates do not return a *
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path
