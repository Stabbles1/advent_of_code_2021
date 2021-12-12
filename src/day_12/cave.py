from typing import List

from dataclasses import dataclass, field

@dataclass
class Cave:
    label: str
    visited: bool = False
    connected_caves: List = field(default_factory=lambda: [])
    
    @property
    def is_visitable(self):
        return True

    def visit(self):
        self.visited = True

    def add_connected_cave(self, cave):
        if cave not in self.connected_caves:
            self.connected_caves.append(cave)

    def __repr__(self):
        representation = f"{self.label} ->"
        # for cave in self.connected_caves:
        #     representation += f" {cave.label} "
        return representation

    def __str__(self):
        representation = f"{self.label} ->"
        # for cave in self.connected_caves:
        #     representation += f" {cave.label} "
        return representation

@dataclass
class SmallCave(Cave):

    @property
    def is_visitable(self):
        return not self.visited

    def __repr__(self):
        representation = f"{self.label} ->"
        # for cave in self.connected_caves:
        #     representation += f" {cave.label} "
        return representation

    def __str__(self):
        representation = f"{self.label} ->"
        # for cave in self.connected_caves:
        #     representation += f" {cave.label} "
        return representation
