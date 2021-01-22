"""
Python Data Structures - A Game-Based Approach
A Star Algorithm maze solver.
Robin Andrews - https://compucademy.net/
Uses a priority queue containing f-values and (i, j) tuples along with dictionaries for
predecessors and g-values.
"""
import os
from helpers import get_path, offsets, is_legal_pos, read_maze
from priority_queue import PriorityQueue


def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze, start, goal):
    """
    create pq
    add start to pq
    predecessor start: none
    g value start: 0
    add while statement for empty pq
    check current_cell is goal
    get path of cell
    for direction loop
    offset the row column
    check neighbor validity
    add g value neighbor = heuristic(start, current_cell)
    add predecessor neighbor = current cell
    add to pq neighbor, priority(current_cell, goal)
    
    """ 
    print(os.getcwd())

    pq = PriorityQueue()
    # The initial priority value doesn't matter since it will be the first one popped
    pq.put(start, 0)

    g = {start: 0}
    predecessors = {start: None}

    while not pq.is_empty():
        current_cell = pq.get()

        if current_cell == goal:
            path = get_path(predecessors, start, goal)
            return path

        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0]+row_offset, current_cell[1]+col_offset) 

            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
                # heuristic of neighbor to goal + distance from start
                # should be the weight
                h = heuristic(neighbor, goal)
                new_cost = g[current_cell] + 1
                f_value = h + new_cost
                
                pq.put(neighbor, f_value)

                g[neighbor] = new_cost
                predecessors[neighbor] = current_cell

    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("08_03_begin/mazes/mini_maze_bfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("08_03_begin/mazes/mini_maze_bfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None
