from typing import Dict, List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list

from puzzle import Puzzle
from puzzle2 import Puzzle2


def input_to_puzzles(lines: List[str], puzzle_type):
    puzzles = []
    for line in lines:
        clues, readings = line.split(" | ")
        puzzles.append(puzzle_type(clues, readings))
    return puzzles


def count_output_value_occurrences(
    puzzles: List[Puzzle], interesting_numbers: List[int]
):
    occurrences = 0
    for puzzle in puzzles:
        for reading in puzzle.get_decoded_readings():
            if reading in interesting_numbers:
                occurrences += 1
    return occurrences


def add_all_outputs(puzzles: List[Puzzle2]):
    total = 0
    for puzzle in puzzles:
        total += puzzle.get_decoded_readings()
    return total


if __name__ == "__main__":
    lines = file_to_list("src/day_8/input")
    puzzles = input_to_puzzles(lines, Puzzle)
    print(
        count_output_value_occurrences(
            puzzles=puzzles, interesting_numbers=[1, 4, 7, 8]
        )
    )

    puzzles = input_to_puzzles(lines, Puzzle2)
    print(add_all_outputs(puzzles=puzzles))
