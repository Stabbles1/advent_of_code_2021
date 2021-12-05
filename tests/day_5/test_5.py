from day_5.part_1 import input_to_vents


sample_input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


def test_input_to_vents():
    vents = input_to_vents(sample_input)
    assert len(vents) == 10
    assert vents[1].x1 == 8
    assert vents[1].y1 == 0
    assert vents[1].x2 == 0
    assert vents[1].y2 == 8



