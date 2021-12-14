from day_14.main import input_to_rules, step, most_common_minus_least_common

input_template = "NNCB"

input_pairs=[
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

def test_step():
    rules = input_to_rules(input_pairs)
    result_1 = step(input_template, rules)
    assert result_1 == "NCNBCHB"

    result_2 = step(result_1, rules, steps=2)
    assert result_2 == "NBBBCNCCNBBNBNBBCHBHHBCHB"

def test_step_1():
    rules = input_to_rules(input_pairs)
    template = step(input_template, rules, 10)
    assert most_common_minus_least_common(template) == 1588

# def test_step_2():
#     rules = input_to_rules(input_pairs)
#     template = step(input_template, rules, 40)
#     assert most_common_minus_least_common(template) == 2188189693529