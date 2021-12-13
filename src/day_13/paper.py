from typing import List, Dict, Tuple
from dataclasses import dataclass, field

from fold import Fold
from dot import Dot

@dataclass
class Paper:
    dots: List = field(default_factory=lambda: [])

    def add_dot(self, dot: Dot):
        if dot not in self.dots:
            self.dots.append(dot)

    def fold(self, fold: Fold):
        for dot in list(self.dots):
            if (fold.orientation == "y" and dot.y > fold.position):
                self.add_dot(Dot(dot.x, dot.y - ((dot.y - fold.position) *2)))
                self.dots.remove(dot)
            elif fold.orientation == "x" and dot.x > fold.position:
                self.add_dot(Dot(dot.x - ((dot.x - fold.position) *2), dot.y))
                self.dots.remove(dot)
