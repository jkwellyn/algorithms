"""
Python Data Structures - A Game-Based Approach
BFS maze solver.
Robin Andrews - https://compucademy.net/
The queue contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from queue_ll import Queue


def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    # bfs, you're dequeueing, checking to see if thats the cell and finding all the neighbors for that cell
    # enqueuing all the neighors
    # adding all the new neighbors into predecessors
    # get path should take the current_cell, look at the value, find the key, get that value
    # keep tracing backwards until the the current cell is the starting cell

    predecessors = {start: None}
    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            path = get_path(predecessors, start, goal)
            return path
        # checking for neighbors
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset, current_cell[1] + col_offset)

            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:

                queue.enqueue(neighbor)
                predecessors[neighbor] = current_cell

    return None

if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # # Test 2
    maze = read_maze("05_02_begin/mazes/mini_maze_bfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("05_02_begin/mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
