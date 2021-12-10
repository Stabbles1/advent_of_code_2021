from typing import Dict, List
import sys
sys.path.insert(0, ".")
from src.common.file_handling import file_to_list

from puzzle import Puzzle

def input_to_puzzles(lines: List[str]):
    puzzles = []
    for line in lines:
        clues, readings = line.split(" | ")
        puzzles.append(Puzzle(clues, readings))
    return puzzles

def count_output_value_occurrences(puzzles:List[Puzzle], interesting_numbers:List[int]):
    occurrences = 0
    for puzzle in puzzles:
        for reading in puzzle.get_decoded_readings():
            if reading in interesting_numbers:
                occurrences += 1

    return occurrences




if __name__ == "__main__":
    lines = file_to_list('src/day_8/input')
    puzzles = input_to_puzzles(lines)
    print(count_output_value_occurrences(puzzles=puzzles, interesting_numbers=[1,4,7,8]))