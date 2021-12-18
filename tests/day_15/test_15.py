from day_15.main import extrapolate_down_right, input_to_cell_maze

test_input = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581",
]

def test_extrapolate_down_right():
    maze = input_to_cell_maze(test_input)
    maze = extrapolate_down_right(maze)
    assert maze[-1][-1].best_risk == 40
