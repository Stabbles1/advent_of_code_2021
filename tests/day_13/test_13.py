from day_13.main import input_to_paper
from day_13.fold import Fold


test_input_dots = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
]

test_input_folds = [
    "fold along y=7",
    "fold along x=5",
]

def test_part_1():
    paper = input_to_paper(test_input_dots)
    assert len(paper.dots) == 18
    paper.fold(Fold("y", 7))
    assert len(paper.dots) == 17
