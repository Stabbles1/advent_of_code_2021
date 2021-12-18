from day_14.main import (
    input_to_rules,
    step,
    most_common_minus_least_common,
    input_template_to_template,
    input_to_character_totals,
)

input_template = "NNCB"

input_pairs = [
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]


def test_input_to_rules():
    rules = input_to_rules(input_pairs)
    assert len(rules) == 16
    assert rules["CH"] == "B"


def test_input_template_to_template():
    template = input_template_to_template(input_template)
    assert len(template) == 3
    print(template)
    assert template["CB"] == 1


def test_step_1():
    rules = input_to_rules(input_pairs)
    template = input_template_to_template(input_template)
    character_totals = input_to_character_totals(input_template)
    step(character_totals, template, rules, steps=10)
    assert most_common_minus_least_common(character_totals) == 1588


def test_step_2():
    rules = input_to_rules(input_pairs)
    template = input_template_to_template(input_template)
    character_totals = input_to_character_totals(input_template)
    step(character_totals, template, rules, steps=40)
    assert most_common_minus_least_common(character_totals) == 2188189693529
