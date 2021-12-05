import sys
import re
from typing import List

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list
from vent import Vent
from map import Map


def input_to_vents(input_lines: List[str]) -> List[Vent]:
    vents = []
    for line in input_lines:
        matches = re.findall(r"\d+", line)
        vents.append(
            Vent(int(matches[0]), int(matches[1]), int(matches[2]), int(matches[3]))
        )
    return vents

if __name__ == "__main__":
    input_lines = file_to_list("src/day_5/input")
    vents = input_to_vents(input_lines)
    
    map = Map()
    for vent in vents:
        if not vent.is_diagonal:
            map.advent(vent)
    
    print(len(map.dangerous_coordinates(danger_threshold=2)))