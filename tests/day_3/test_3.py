from day_3.part_1 import calculate_gamma, calculate_epsilon, calculate_power_consumption

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
    gamma = calculate_gamma(diagnostics)
    assert gamma == '10110'
    epsilon = calculate_epsilon(gamma)
    assert epsilon == '01001'
    power_conumption = calculate_power_consumption(gamma, epsilon)
    assert power_conumption == 198
