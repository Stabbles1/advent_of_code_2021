from dataclasses import dataclass


@dataclass
class Vent:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def is_diagonal(self):
        return not (self.x1 == self.x2 or self.y1 == self.y2)

    def calculate_all_coordinates(self):
        coordinates = []
        x_delta = self.x1 - self.x2
        y_delta = self.y1 - self.y2
        x_direction = 1 if self.x1 < self.x2 else -1
        y_direction = 1 if self.y1 < self.y2 else -1
        if x_delta == 0:
            for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                coordinates.append(f"{self.x1},{y}")
        elif y_delta == 0:
            for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
                coordinates.append(f"{x},{self.y1}")
        else:
            for x, y in zip(
                range(self.x1, self.x2 + x_direction, x_direction),
                range(self.y1, self.y2 + y_direction, y_direction),
            ):
                coordinates.append(f"{x},{y}")
        return coordinates
