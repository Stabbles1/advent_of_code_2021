from typing import List
from dataclasses import dataclass
import re

GRID_SIZE = 5


@dataclass
class Square:
    number: int
    x_position: int
    y_position: int
    marked: bool = False

    def mark(self):
        self.marked = True


class Grid:
    def __init__(self, raw_grid: List[str]):
        self.solved = False
        self.score = 0
        self.squares = self.populate_squares(raw_grid)

    def populate_squares(self, raw_grid) -> List[Square]:
        squares = []
        for row, y_position in zip(raw_grid, range(GRID_SIZE)):
            matches = re.findall(r"\d+", row)
            for match, x_position in zip(matches, range(GRID_SIZE)):
                squares.append(
                    Square(
                        number=int(match), x_position=x_position, y_position=y_position
                    )
                )
        return squares

    def mark_number(self, number: int):
        for square in self.squares:
            if number == square.number:
                square.mark()
                self.update_solved_status()
        if self.solved:
            self.update_score(winning_number=number)

    def update_solved_status(self):
        x_tracker = {x: 0 for x in range(GRID_SIZE)}
        y_tracker = {y: 0 for y in range(GRID_SIZE)}
        for square in self.squares:
            if square.marked:
                x_tracker[square.x_position] += 1
                y_tracker[square.y_position] += 1

        if GRID_SIZE in x_tracker.values() or GRID_SIZE in y_tracker.values():
            self.solved = True

    def update_score(self, winning_number):
        unmarked_total = 0
        for square in self.squares:
            if square.marked == False:
                unmarked_total += square.number
        self.score = unmarked_total * winning_number
