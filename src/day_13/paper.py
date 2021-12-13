from typing import List, Dict, Tuple
from dataclasses import dataclass, field

from fold import Fold

@dataclass
class Paper:
    dots: Dict = field(default_factory=lambda: {})

    def add_dot(self, coords: (int, int)):
        self.dots[coords] = 1

    def fold(self, fold: Fold):
        for x, y in list(self.dots.keys()):
            if (fold.orientation == "y" and y > fold.position):
                self.add_dot((x, y - ((y - fold.position) *2)))
                del self.dots[x,y]
            elif fold.orientation == "x" and x > fold.position:
                self.add_dot(((x - (x - fold.position) *2), y))
                del self.dots[x,y]
