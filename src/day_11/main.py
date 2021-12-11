from typing import List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list

from octopus import Octopus
from octopus_grid import OctopusGrid

def input_to_octopus_grid(raw_input):
    rows = []
    for row in raw_input:
        cols = []
        for num in row:
            cols.append(Octopus(int(num)))
        rows.append(cols)
    return OctopusGrid(rows)

if __name__ == "__main__":
    lines = file_to_list("src/day_11/input")
    octopus_grid = input_to_octopus_grid(lines)
    print(octopus_grid.run_steps(100))
