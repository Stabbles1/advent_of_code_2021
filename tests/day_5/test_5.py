from day_5.main import input_to_vents
from day_5.map import Map


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

def test_part_1_solution():
    vents = input_to_vents(sample_input)
    map = Map()
    for vent in vents:
        if not vent.is_diagonal:
            map.advent(vent)
    assert len(map.dangerous_coordinates(danger_threshold=2)) == 5

def test_part_2_solution():
    vents = input_to_vents(sample_input)
    map = Map()
    for vent in vents:
        map.advent(vent)
    
    print(map.dangerous_coordinates(danger_threshold=2))
    assert len(map.dangerous_coordinates(danger_threshold=2)) == 12