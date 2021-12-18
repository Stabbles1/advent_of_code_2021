from typing import List, Dict
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list

from cell import Cell


def input_to_maze(raw_input):
    maze = []
    for row in raw_input:
        maze_row = []
        for num in row:
            maze_row.append(Cell(int(num)))
        maze.append(maze_row)
    return maze

def input_to_mega_maze(raw_input, magnification=5):
    maze = []
    for row_count, row in enumerate(raw_input * magnification):
        maze_row = []
        for col_count, num in enumerate(row * magnification):
            maze_row.append(Cell(calculate_mofified_risk(row_count, col_count, len(raw_input), num)))
        maze.append(maze_row)
    return maze

def calculate_mofified_risk(row_count, col_count, orig_size, orig_risk):
    modifier = int(row_count / orig_size)
    modifier += int(col_count / orig_size)
    if (int(orig_risk) + modifier) % 9 == 0:
        return 9
    return (int(orig_risk) + modifier) % 9

def extrapolate(maze):
    still_calculating = True
    while still_calculating:
        still_calculating = False
        for depth in range(len(maze) * 2):
            for x, y in zip(range(depth + 1), range(depth, -1, -1)):
                try:
                    if x == 0 and y == 0:
                        maze[x][y].offer_better_risk(0)
                    if x - 1 >= 0:
                        still_calculating = maze[x][y].offer_better_risk(maze[x - 1][y].best_risk + maze[x][y].risk) or still_calculating
                    if y - 1 >= 0:
                        still_calculating = maze[x][y].offer_better_risk(maze[x][y - 1].best_risk + maze[x][y].risk) or still_calculating
                    if x + 1 < len(maze):
                        still_calculating = maze[x][y].offer_better_risk(maze[x + 1][y].best_risk + maze[x][y].risk) or still_calculating
                    if y + 1 < len(maze):
                        still_calculating = maze[x][y].offer_better_risk(maze[x][y + 1].best_risk + maze[x][y].risk) or still_calculating
                except IndexError:
                    pass
                    #Out of bounds
    return maze


if __name__ == "__main__":
    raw_input = file_to_list("src/day_15/input")
    maze = input_to_maze(raw_input)
    maze = extrapolate(maze)
    print(maze[-1][-1].best_risk)

    mega_maze = input_to_mega_maze(raw_input)
    mega_maze = extrapolate(mega_maze)
    print(mega_maze[-1][-1].best_risk)
