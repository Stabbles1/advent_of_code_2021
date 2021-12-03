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


def calculate_column_dominance(
    diagnostics, column=0, tie_breaker="1", least_common_wins=False
) -> str:
    running_total = 0
    for rating in diagnostics:
        running_total += int(rating[column])
    if running_total == len(diagnostics) / 2:
        return tie_breaker
    elif running_total > len(diagnostics) / 2:
        return "0" if least_common_wins else "1"
    return "1" if least_common_wins else "0"


def calculate_epsilon(gamma: str):
    return "".join("0" if bit == "1" else "1" for bit in gamma)


def calculate_gas_rating(
    diagnostics: List[str], tie_breaker: str, least_common_wins: bool
):
    for bit_index in range(len(diagnostics)):
        dominant_bit = calculate_column_dominance(
            diagnostics=diagnostics,
            column=bit_index,
            tie_breaker=tie_breaker,
            least_common_wins=least_common_wins,
        )
        diagnostics = [
            rating for rating in diagnostics if rating[bit_index] == dominant_bit
        ]
        if len(diagnostics) == 1:
            return diagnostics[0]


def multiply_ratings(rating_1: str, rating_2: str):
    return int(rating_1, 2) * int(rating_2, 2)


diagnostics = file_to_list("src/day_3/input")
gamma = calculate_gamma(diagnostics)
epsilon = calculate_epsilon(gamma)
print(multiply_ratings(gamma, epsilon))
o2 = calculate_gas_rating(
    diagnostics=diagnostics, tie_breaker="1", least_common_wins=False
)
co2 = calculate_gas_rating(
    diagnostics=diagnostics, tie_breaker="0", least_common_wins=True
)
print(multiply_ratings(o2, co2))
