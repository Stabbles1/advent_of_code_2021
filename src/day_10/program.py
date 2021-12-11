from typing import List

from chunk_line import ChunkLine
from chunk_character import ChunkCharacter


class Program:
    def __init__(self, chunk_lines: List[ChunkLine]):
        self.chunk_lines = chunk_lines
        self.corrupt_tally = corrupt_tally = {
            ")": ChunkCharacter("(", ")", 3),
            "]": ChunkCharacter("[", "]", 57),
            "}": ChunkCharacter("{", "}", 1197),
            ">": ChunkCharacter("<", ">", 25137),
        }

    def calculate_corrupt_score(self):
        corrupt_lines = [line for line in self.chunk_lines if line.is_corrupt()]
        for corrupt_line in corrupt_lines:
            self.corrupt_tally[corrupt_line.corrupt_character].increment()

        total = 0
        for corrupt_char in self.corrupt_tally.values():
            total += corrupt_char.corrupt_points * corrupt_char.count
        return total

    def calculate_incomplete_score(self):
        # By taking the median of all scores in the program
        self.remove_corrupt_lines()
        scores = []
        for line in self.chunk_lines:
            scores.append(line.completion_score())
        scores.sort()
        return scores[int(len(scores)/2)]


        
    def remove_corrupt_lines(self):
        for line in list(self.chunk_lines):
            if line.is_corrupt():
                self.chunk_lines.remove(line)
