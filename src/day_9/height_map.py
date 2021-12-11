from typing import List

from height_point import HeightPoint
from basin import Basin


class HeightMap:
    def __init__(self, height_points: List[List[HeightPoint]]):
        self.points = height_points
        self.map_height = len(height_points)
        self.map_width = len(height_points[0])
        self.basins = []

    def mark_basins(self):
        for row_index, row in enumerate(self.points):
            for col_index, point in enumerate(row):
                if point.height < 9 and point.basin is None:
                    point.basin = Basin()
                    self.basins.append(point.basin)
                    self.expand_basin(row_index, col_index, point.basin)

    def expand_basin(self, row_index, col_index, basin):
        if row_index != 0:  # We should check above
            if (
                self.points[row_index - 1][col_index].height < 9
                and self.points[row_index - 1][col_index].basin is None
            ):
                basin.size += 1
                self.points[row_index - 1][col_index].basin = basin
                self.expand_basin(row_index - 1, col_index, basin)
        if row_index != self.map_height - 1:  # We should check below
            if (
                self.points[row_index + 1][col_index].height < 9
                and self.points[row_index + 1][col_index].basin is None
            ):
                basin.size += 1
                self.points[row_index + 1][col_index].basin = basin
                self.expand_basin(row_index + 1, col_index, basin)
        if col_index != 0:  # We should check left
            if (
                self.points[row_index][col_index - 1].height < 9
                and self.points[row_index][col_index - 1].basin is None
            ):
                basin.size += 1
                self.points[row_index][col_index - 1].basin = basin
                self.expand_basin(row_index, col_index - 1, basin)
        if col_index != self.map_width - 1:  # We should check right
            if (
                self.points[row_index][col_index + 1].height < 9
                and self.points[row_index][col_index + 1].basin is None
            ):
                basin.size += 1
                self.points[row_index][col_index + 1].basin = basin
                self.expand_basin(row_index, col_index + 1, basin)

    def multiply_largest_basins(self, top=3):
        total = 1
        self.basins.sort(key=lambda basin: basin.size, reverse=True)
        for index in range(top):
            total = total * self.basins[index].size
        return total

    def mark_low_points(self):
        for row_index, row in enumerate(self.points):
            for col_index, point in enumerate(row):
                point.low_point = self.check_if_low_point(row_index, col_index)

    def check_if_low_point(self, row_index, col_index):
        if row_index != 0:  # We should check above
            if (
                self.points[row_index - 1][col_index].height
                <= self.points[row_index][col_index].height
            ):
                return False
        if row_index != self.map_height - 1:  # We should check below
            if (
                self.points[row_index + 1][col_index].height
                <= self.points[row_index][col_index].height
            ):
                return False
        if col_index != 0:  # We should check left
            if (
                self.points[row_index][col_index - 1].height
                <= self.points[row_index][col_index].height
            ):
                return False
        if col_index != self.map_width - 1:  # We should check right
            if (
                self.points[row_index][col_index + 1].height
                <= self.points[row_index][col_index].height
            ):
                return False
        return True

    def low_point_risk_total(self):
        total = 0
        for row in self.points:
            for point in row:
                total += point.risk_level
        return total
