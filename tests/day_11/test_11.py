from day_11.main import input_to_octopus_grid

test_input = [
"5483143223",
"2745854711",
"5264556173",
"6141336146",
"6357385478",
"4167524645",
"2176841721",
"6882881134",
"4846848554",
"5283751526",
]

def test_input_to_octopus_grid():
    octopus_grid = input_to_octopus_grid(test_input)
    assert len(octopus_grid.grid) == 10
    assert len(octopus_grid.grid[0]) == 10
    assert octopus_grid.grid[0][0].energy_level == 5

def test_part_1():
    octopus_grid = input_to_octopus_grid(test_input)
    assert octopus_grid.run_steps(100) == 1656

def test_part_2():
    octopus_grid = input_to_octopus_grid(test_input)
    assert octopus_grid.steps_until_all_flash() == 195