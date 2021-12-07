from typing import Dict, List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_int_list

def most_efficient_position(crab_positions: List[int]):
    remaining_range = list(range(0, max(crab_positions) + 1))
    while True:
        remaining_range = most_efficient_half(crab_positions, remaining_range)
        if len(remaining_range) == 1:
            break
    return remaining_range[0]

def most_efficient_half(crab_positions: List[int], remaining_range: List[int]):
    mid_point = int(len(remaining_range)/2)
    option_1 = remaining_range[mid_point-1]
    option_2 = remaining_range[mid_point]
    fuel_for_option_1 = fuel_required_actual(crab_positions, option_1)
    fuel_for_option_2 = fuel_required_actual(crab_positions, option_2)
    print(f"{option_1=} {fuel_for_option_1=} {option_2=} {fuel_for_option_2=}")
    if fuel_for_option_1 < fuel_for_option_2:
        return remaining_range[:mid_point]
    else:
        return remaining_range[mid_point:]

def fuel_required(crab_positions: List[int], target_location: int) -> int:
    fuel_used = 0
    for position in crab_positions:
        fuel_used += abs(position - target_location)
    return fuel_used

def fuel_required_actual(crab_positions: List[int], target_location: int) -> int:
    print(crab_positions)
    fuel_used = 0
    for position in crab_positions:
        distance = 0
        distance += abs(position - target_location)
        fuel_used += (distance**2 + distance) / 2
    return int(fuel_used)

if __name__ == "__main__":
    crab_positions = file_to_int_list('src/day_7/input')
    mep = most_efficient_position(crab_positions)
    print(fuel_required_actual(crab_positions, mep))