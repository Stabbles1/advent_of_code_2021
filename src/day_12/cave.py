from typing import List

from dataclasses import dataclass, field

@dataclass
class Cave:
    label: str
    connected_caves: List = field(default_factory=lambda: [])

    def add_connected_cave(self, cave):
        if cave not in self.connected_caves:
            self.connected_caves.append(cave)
