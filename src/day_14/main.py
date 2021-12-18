from typing import List, Dict
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list


def input_to_rules(raw_input):
    rules = {}
    for line in raw_input:
        key, value = line.split(" -> ")
        rules[key] = value
    return rules


def input_template_to_template(raw_input):
    template = {}
    for index in range(len(raw_input) - 1):
        pair = raw_input[index] + raw_input[index + 1]
        template[pair] = template.get(pair, 0) + 1
    return template


def input_to_character_totals(raw_input):
    character_totals = {}
    for char in raw_input:
        character_totals[char] = character_totals.get(char, 0) + 1
    return character_totals


def step(
    character_totals: Dict[str, int],
    template: Dict[str, int],
    rules: Dict[str, str],
    steps=1,
):
    if steps == 0:
        return character_totals
    new_template = {}
    for key, value in template.items():
        new_template[key[0] + rules[key]] = (
            new_template.get(key[0] + rules[key], 0) + value
        )
        new_template[rules[key] + key[1]] = (
            new_template.get(rules[key] + key[1], 0) + value
        )
        character_totals[rules[key]] = character_totals.get(rules[key], 0) + value
    return step(character_totals, new_template, rules, steps - 1)


def most_common_minus_least_common(character_totals: Dict[str, int]):
    most_common = float("-inf")
    least_common = float("+inf")

    for count in character_totals.values():
        if count > most_common:
            most_common = count
        if count < least_common:
            least_common = count

    return most_common - least_common


if __name__ == "__main__":
    input_rules = file_to_list("src/day_14/input_rules")
    input_template = file_to_list("src/day_14/input_template")[0]
    rules = input_to_rules(input_rules)
    template = input_template_to_template(input_template)
    character_totals = input_to_character_totals(input_template)
    print(most_common_minus_least_common(step(character_totals, template, rules, 40)))
