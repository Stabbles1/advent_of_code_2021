from typing import List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list


def calculate_gamma(diagnostics: List[str]):
    running_total = []
    for rating in diagnostics:
        if len(running_total) == 0:
            running_total = [int(bit) for bit in rating]
        else:
            for bit_index in range(len(rating)):
                running_total[bit_index] += int(rating[bit_index])
    return "".join(
        "0" if bit_total < len(diagnostics) / 2 else "1" for bit_total in running_total
    )


def calculate_epsilon(gamma: str):
    return "".join("0" if bit == "1" else "1" for bit in gamma)


def calculate_power_consumption(gamma: str, epsilon: str):
    return int(gamma, 2) * int(epsilon, 2)


diagnostics = file_to_list("src/day_3/input")
gamma = calculate_gamma(diagnostics)
epsilon = calculate_epsilon(gamma)
print(calculate_power_consumption(gamma, epsilon))
