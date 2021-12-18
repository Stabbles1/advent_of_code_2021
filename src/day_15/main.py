from typing import List, Dict
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list

from cell import Cell


def input_to_cell_maze(raw_input):
    maze = []
    for row in raw_input:
        maze_row = []
        for num in row:
            maze_row.append(Cell(int(num)))
        maze.append(maze_row)
    return maze


def extrapolate_down_right(maze):
    for depth in range(len(maze) * 2):
        for x, y in zip(range(depth + 1), range(depth, -1, -1)):
            try:
                if x == 0 and y == 0:
                    maze[x][y].offer_better_risk(0)
                if x - 1 >= 0:
                    maze[x][y].offer_better_risk(maze[x - 1][y].best_risk + maze[x][y].risk)
                if y - 1 >= 0:
                    maze[x][y].offer_better_risk(maze[x][y - 1].best_risk + maze[x][y].risk)
            except IndexError:
                pass
                #Out of bounds
    #print_maze(maze)
    return maze

def print_maze(maze):
    string = ""
    for row in maze:
        string += "\n"
        for cell in row:
            if cell.best_risk >= 100:
                string += f" {cell.best_risk} "
            elif cell.best_risk >= 10:
                string += f" {cell.best_risk}  "
            else:
                string += f" {cell.best_risk}   "
    print(string)

if __name__ == "__main__":
    raw_input = file_to_list("src/day_15/input")
    maze = input_to_cell_maze(raw_input)
    maze = extrapolate_down_right(maze)
    print(maze[-1][-1].best_risk)