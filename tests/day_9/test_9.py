from day_9.main import input_to_height_map

test_input = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]


def test_input_to_height_map():
    height_map = input_to_height_map(test_input)
    assert height_map.points[0][0].height == 2
    assert height_map.points[0][0].low_point == False
    assert height_map.points[1][2].height == 8


def test_part_1():
    height_map = input_to_height_map(test_input)
    height_map.mark_low_points()
    assert height_map.low_point_risk_total() == 15


def test_part_2():
    height_map = input_to_height_map(test_input)
    height_map.mark_basins()
    assert len(height_map.basins) == 4

    for basin, expected_size in zip(height_map.basins, [3, 9, 14, 9]):
        assert basin.size == expected_size

    assert height_map.multiply_largest_basins() == 1134
