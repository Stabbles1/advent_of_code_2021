from day_7.main import (
    most_efficient_half,
    fuel_required,
    most_efficient_position,
    fuel_required_actual,
)

crab_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_most_efficient_half_is_returned():
    remaining_range = list(range(0, max(crab_positions) + 1))
    result = most_efficient_half(
        crab_positions=crab_positions, remaining_range=remaining_range
    )
    print(f"{remaining_range=} {crab_positions=} {result=}")
    assert result == [0, 1, 2, 3, 4, 5, 6, 7]


def test_fuel_required():
    assert fuel_required(crab_positions, 2) == 37


def test_fuel_required_actual():
    assert fuel_required_actual(crab_positions, 2) == 206
    assert fuel_required_actual(crab_positions, 5) == 168


def test_most_efficient_position():
    assert most_efficient_position(crab_positions) == 2
    assert most_efficient_position([1, 2, 3]) == 2
    assert most_efficient_position([1, 2, 3, 4]) in [2, 3]
    assert most_efficient_position([1, 2, 3, 4, 1]) == 2
    assert most_efficient_position([1, 2, 3, 4, 1, 2]) == 2
