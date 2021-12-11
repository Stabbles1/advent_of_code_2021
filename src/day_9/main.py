from typing import List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list

from height_map import HeightMap
from height_point import HeightPoint


def input_to_height_map(raw_input: List[str]):
    all_height_points = []
    for line in raw_input:
        row_height_points = []
        for number in line:
            row_height_points.append(HeightPoint(int(number)))
        all_height_points.append(row_height_points)
    return HeightMap(all_height_points)


if __name__ == "__main__":
    lines = file_to_list("src/day_9/input")
    height_map = input_to_height_map(lines)
    height_map.mark_low_points()
    print(height_map.low_point_risk_total())
    height_map.mark_basins()
    print(height_map.multiply_largest_basins())
