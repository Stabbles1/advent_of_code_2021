from typing import List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list

from chunk_line import ChunkLine


def input_to_chunk_lines(raw_input):
    return [ChunkLine(line) for line in raw_input]


def calculate_corrupt_score(chunk_lines: List[ChunkLine]):
    corrupt_lines = [line for line in chunk_lines if line.is_corrupt()]
    corrupt_tally = {
        ")": 0,
        "]": 0,
        "}": 0,
        ">": 0,
    }

    for corrupt_line in corrupt_lines:
        corrupt_tally[corrupt_line.corrupt_character] += 1
    return sum((corrupt_tally[")"] * 3, corrupt_tally["]"] * 57, corrupt_tally["}"] * 1197, corrupt_tally[">"] * 25137))


if __name__ == "__main__":
    lines = file_to_list("src/day_10/input")
    chunk_lines = input_to_chunk_lines(lines)
    print(calculate_corrupt_score(chunk_lines))
