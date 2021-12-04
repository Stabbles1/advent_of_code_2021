from typing import List
from grid import Grid, GRID_SIZE
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list, file_to_int_list

def construct_grids(raw_grids):
    grids = []
    for i in range(0, len(raw_grids), GRID_SIZE+1):
        grids.append(Grid(raw_grids[i:i+GRID_SIZE]))
    return grids

def score_of_winning_board(grids: List[Grid], called_numbers: List[int]):
    for number in called_numbers:
        print(number)
        for grid in grids:
            grid.mark_number(number)
            if grid.solved:
                print(grid.squares)
                return grid.score

called_numbers = file_to_int_list("src/day_4/input_called_numbers")
raw_grids = file_to_list("src/day_4/input_grids")
grids = construct_grids(raw_grids)
print(score_of_winning_board(grids, called_numbers))
