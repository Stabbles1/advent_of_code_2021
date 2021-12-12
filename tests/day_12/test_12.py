from day_12.cave_system import CaveSystem
from day_12.cave import Cave
from day_12.main import input_to_populated_cave_system

test_input_tiny = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
]
test_input_small = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]

test_input_large = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW",
]


def test_cave_system_can_be_built():
    cave_system = CaveSystem()
    cave_system.add_cave_link(
        Cave("start"),
        Cave("A"),
    )

    assert len(cave_system.caves) == 2
    cave_system.add_cave_link(
        Cave("A"),
        Cave("end"),
    )

    assert len(cave_system.caves) == 3


def test_input_to_cave_system():
    cave_system = input_to_populated_cave_system(test_input_tiny)
    assert len(cave_system.caves) == 6
    assert len(cave_system.caves["A"].connected_caves) == 4
    assert cave_system.caves["A"] in cave_system.caves["b"].connected_caves


def test_cave_system_can_calculate_all_routes():
    test_input = [
        "start-A",
        "A-end",
    ]
    cave_system = input_to_populated_cave_system(test_input)
    cave_system.find_all_routes("start", [])
    assert cave_system.journeys == [["start", "A", "end"]]

    print("--" * 20)
    test_input = [
        "start-A",
        "A-b",
        "b-end",
    ]
    cave_system = input_to_populated_cave_system(test_input)
    cave_system.find_all_routes("start", [])
    assert cave_system.journeys == [["start", "A", "b", "end"]]

    print("--" * 20)
    test_input = [
        "start-A",
        "A-b",
        "A-end",
    ]
    cave_system = input_to_populated_cave_system(test_input)
    cave_system.find_all_routes("start", [])
    assert cave_system.journeys == [
        ["start", "A", "b", "A", "end"],
        ["start", "A", "end"],
    ]


def test_part_1():
    tiny_cave_system = input_to_populated_cave_system(test_input_tiny)
    tiny_cave_system.find_all_routes("start", [])
    assert len(tiny_cave_system.journeys) == 10

    cave_system = input_to_populated_cave_system(test_input_small)
    cave_system.find_all_routes("start", [])
    assert len(cave_system.journeys) == 19

    large_cave_system = input_to_populated_cave_system(test_input_large)
    large_cave_system.find_all_routes("start", [])
    assert len(large_cave_system.journeys) == 226


def test_part_2():
    tiny_cave_system = input_to_populated_cave_system(test_input_tiny)
    tiny_cave_system.find_all_routes_part_2("start", [])
    assert len(tiny_cave_system.journeys) == 36

    cave_system = input_to_populated_cave_system(test_input_small)
    cave_system.find_all_routes_part_2("start", [])
    assert len(cave_system.journeys) == 103

    large_cave_system = input_to_populated_cave_system(test_input_large)
    large_cave_system.find_all_routes_part_2("start", [])
    assert len(large_cave_system.journeys) == 3509


def test_small_visit_is_unused():
    assert CaveSystem.small_visit_is_unused(["start", "A"])
    assert CaveSystem.small_visit_is_unused(["start", "A", "b"])
    assert CaveSystem.small_visit_is_unused(["start", "A", "b", "A"])
    assert not CaveSystem.small_visit_is_unused(["start", "A", "b", "A", "b"])
