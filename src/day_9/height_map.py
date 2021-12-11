from typing import List

from point import Point
from basin import Basin


class HeightMap:
    def __init__(self, points: List[List[Point]]):
        self.points = points
        self.map_height = len(points)
        self.map_width = len(points[0])
        self.basins = []

    def mark_basins(self):
        for row_index, row in enumerate(self.points):
            for col_index, point in enumerate(row):
                if point.height < 9 and point.basin is None:
                    point.basin = Basin()
                    self.basins.append(point.basin)
                    self.expand_basin(row_index, col_index, point.basin)

    def get_checkable_directions(self, row_index, col_index):
        # To handle locations around the edge of the map
        checkable_directions = []
        if row_index != 0:
            checkable_directions.append((row_index - 1, col_index))
        if row_index != self.map_height - 1:
            checkable_directions.append((row_index + 1, col_index))
        if col_index != 0:
            checkable_directions.append((row_index, col_index - 1))
        if col_index != self.map_width - 1:
            checkable_directions.append((row_index, col_index + 1))
        return checkable_directions

    def expand_basin(self, row_index, col_index, basin):
        for row_index_to_check, col_index_to_check in self.get_checkable_directions(
            row_index, col_index
        ):
            if (
                self.points[row_index_to_check][col_index_to_check].height < 9
                and self.points[row_index_to_check][col_index_to_check].basin is None
            ):
                basin.size += 1
                self.points[row_index_to_check][col_index_to_check].basin = basin
                self.expand_basin(row_index_to_check, col_index_to_check, basin)

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
        for row_index_to_check, col_index_to_check in self.get_checkable_directions(
            row_index, col_index
        ):
            if (
                self.points[row_index_to_check][col_index_to_check].height
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
