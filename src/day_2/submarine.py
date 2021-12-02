from dataclasses import dataclass

@dataclass
class Submarine():
    colour: str
    depth: int = 0
    distance: int = 0
    aim: int = 0

    def move(self, direction, magnitude):
        if direction == "forward":
            self.distance += magnitude
            self.depth += self.aim * magnitude
        elif direction == "down":
            self.aim += magnitude
        elif direction == "up":
            self.aim -= magnitude
