from typing import Dict
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_int_list


def proceed_one_day(initial_fish: Dict[int,int]) -> Dict[int,int]:
    final_fish = {}
    for age, population in initial_fish.items():
        if age == 0:
            final_fish[8] = final_fish.get(8,0) + population
            final_fish[6] = final_fish.get(6,0) + population
        else:
            final_fish[age-1] = final_fish.get(age-1,0) + population
    return final_fish

fish_list = file_to_int_list('src/day_6/input')

population_by_age = { index:fish_list.count(index) for index in range(0,9) }

for i in range(256):
    population_by_age = proceed_one_day(population_by_age)
    print(f"{i=} {sum(population_by_age.values())=}")
