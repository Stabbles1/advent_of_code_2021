from typing import List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list

from cave_system import CaveSystem
from cave import Cave

def input_to_populated_cave_system(raw_input):
    cave_system = CaveSystem()
    for line in raw_input:
        cave_couple = []
        for label in line.split("-"):
            cave_couple.append(Cave(label))
        cave_system.add_cave_link(cave_couple[0], cave_couple[1])
    return cave_system


if __name__ == "__main__":
    lines = file_to_list("src/day_12/input")
    cave_system = input_to_populated_cave_system(lines)
    cave_system.find_all_routes("start", [])
    print(len(cave_system.journeys))
    
    cave_system_part_2 = input_to_populated_cave_system(lines)
    cave_system_part_2.find_all_routes_part_2("start", [])
    print(len(cave_system_part_2.journeys))