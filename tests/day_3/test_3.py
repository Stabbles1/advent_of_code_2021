from day_3 import part_1_and_2


def test_with_sample_data():
    diagnostics = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    gamma = part_1_and_2.calculate_gamma(diagnostics)
    assert gamma == "10110"
    epsilon = part_1_and_2.calculate_epsilon(gamma)
    assert epsilon == "01001"
    power_conumption = part_1_and_2.multiply_ratings(gamma, epsilon)
    assert power_conumption == 198
    o2_rating = part_1_and_2.calculate_gas_rating(
        diagnostics=diagnostics, tie_breaker="1", least_common_wins=False
    )
    assert o2_rating == "10111"
    co2_rating = part_1_and_2.calculate_gas_rating(
        diagnostics=diagnostics, tie_breaker="0", least_common_wins=True
    )
    assert co2_rating == "01010"
    life_support_rating = part_1_and_2.multiply_ratings(o2_rating, co2_rating)
    assert life_support_rating == 230
