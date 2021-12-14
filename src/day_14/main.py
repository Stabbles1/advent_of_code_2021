from typing import List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list


def input_to_rules(raw_input):
    rules = {}
    for line in raw_input:
        key, value = line.split(" -> ")
        rules[key] = value
    return rules

def step(template, rules, steps=1):
    if steps == 0:
        return template
    new_template = ""
    for index in range(len(template)):
        try:
            new_template += template[index]
            new_template += rules[template[index] + template[index+1]]
        except IndexError:
            return step(new_template, rules, steps-1)

def most_common_minus_least_common(template):
    character_counts = {}
    for element in template:
        character_counts[element] = character_counts.get(element, 1) + 1

    most_common = float("-inf")
    least_common = float("+inf")

    for count in character_counts.values():
        if count > most_common:
            most_common = count
        if count < least_common:
            least_common = count

    return most_common - least_common

if __name__ == "__main__":
    input_rules = file_to_list("src/day_14/input_rules")
    template = file_to_list("src/day_14/input_template")[0]
    rules = input_to_rules(input_rules)
    print(most_common_minus_least_common(step(template, rules, 10)))
