from day_4.grid import Grid
from day_4.part_1_and_2 import construct_grids, score_of_winning_board, score_of_losing_board

called_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

raw_grids = [
"22 13 17 11  0",
" 8  2 23  4 24",
"21  9 14 16  7",
" 6 10  3 18  5",
" 1 12 20 15 19",
"",
" 3 15  0  2 22",
" 9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",
"",
"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
" 2  0 12  3  7"]

def test_grid_can_be_created():
    grid = Grid(raw_grids[0:5])
    assert len(grid.squares) == 25
    assert grid.squares[5].number == 8
    assert grid.squares[5].x_position == 0
    assert grid.squares[5].y_position == 1
    assert grid.squares[5].marked == False

def test_number_can_be_marked():
    grid = Grid(raw_grids[0:5])
    grid.mark_number(13)
    assert grid.squares[1].number == 13
    assert grid.squares[1].marked == True

def test_grid_gets_marked_as_solved_for_column_win():
    grid = Grid(raw_grids[0:5])
    grid.mark_number(17)
    grid.mark_number(23)
    grid.mark_number(14)
    grid.mark_number(3)
    assert grid.solved == False
    grid.mark_number(20)
    assert grid.solved == True

def test_grid_gets_marked_as_solved_for_row_win():
    grid = Grid(raw_grids[0:5])
    grid.mark_number(1)
    grid.mark_number(12)
    grid.mark_number(20)
    grid.mark_number(15)
    assert grid.solved == False
    grid.mark_number(19)
    assert grid.solved == True

def test_all_grids_created_from_raw_input():
    grids = construct_grids(raw_grids)
    assert len(grids) == 3

def test_find_score_of_winning_board():
    grids = construct_grids(raw_grids)
    assert score_of_winning_board(grids, called_numbers) == 4512
    
def test_find_score_of_losing_board():
    grids = construct_grids(raw_grids)
    assert score_of_losing_board(grids, called_numbers) == 1924
