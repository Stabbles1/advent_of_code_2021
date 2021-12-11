from typing import List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list

from chunk_line import ChunkLine
from program import Program


def input_to_program(raw_input):
    return Program([ChunkLine(line) for line in raw_input])

if __name__ == "__main__":
    lines = file_to_list("src/day_10/input")
    
    program = input_to_program(lines)
    print(program.calculate_corrupt_score())
    print(program.calculate_incomplete_score())
