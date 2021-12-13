from typing import List
import sys

sys.path.insert(0, ".")
from src.common.file_handling import file_to_list
from paper import Paper
from fold import Fold

def input_to_paper(input_dots):
    paper = Paper()
    for line in input_dots:
        paper.add_dot(tuple(map(int, line.split(","))))
    return paper

def input_to_folds(input_folds):
    folds: Fold = []
    for line in input_folds:
        line = line.replace("fold along ", "")
        orientation, position = line.split("=")
        folds.append(Fold(orientation, int(position)))
    return folds


if __name__ == "__main__":
    input_dots = file_to_list("src/day_13/input_dots")
    input_folds = file_to_list("src/day_13/input_folds")
    paper = input_to_paper(input_dots)
    folds = input_to_folds(input_folds)
    
    paper.fold(folds[0])
    
    print(len(paper.dots))
