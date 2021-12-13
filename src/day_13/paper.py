from typing import List, Dict, Tuple
from dataclasses import dataclass, field

from fold import Fold

@dataclass
class Paper:
    dots: Dict = field(default_factory=lambda: {})

    def add_dot(self, coords: (int, int)):
        self.dots[coords] = 1

    def fold(self, fold: Fold):
        dots_to_move = self.find_dots_to_move(fold)
        for dot_to_move in dots_to_move:
            self.move_dot(dot_to_move, fold)


    def find_dots_to_move(self, fold: Fold):
        dots_to_move: List[int, int] = []
        for x, y in self.dots.keys():
            if ((fold.orientation == "y" and y > fold.position) 
            or (fold.orientation == "x" and x > fold.position)):
                dots_to_move.append((x,y))
        return dots_to_move

    def move_dot(self, xy, fold: Fold):
        x = xy[0]
        y = xy[1]
        if fold.orientation == "y":
            self.add_dot((x, y - ((y - fold.position) *2)))
            del self.dots[x,y]
        else:
            self.add_dot(((x - (x - fold.position) *2), y))
            del self.dots[x,y]
