from typing import List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list

from height_map import HeightMap
from point import Point


def input_to_height_map(raw_input: List[str]):
    all_points = []
    for line in raw_input:
        row_points = []
        for number in line:
            row_points.append(Point(int(number)))
        all_points.append(row_points)
    return HeightMap(all_points)


if __name__ == "__main__":
    lines = file_to_list("src/day_9/input")
    height_map = input_to_height_map(lines)
    height_map.mark_low_points()
    print(height_map.low_point_risk_total())
    height_map.mark_basins()
    print(height_map.multiply_largest_basins())
