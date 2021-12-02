import sys
sys.path.insert(0,'.')
from common.file_handling import file_to_list
from submarine import Submarine

movements = file_to_list("2/input")
sub = Submarine(colour="yellow")

for movement in movements:
    direction, magnitude = movement.split(" ")
    sub.move(direction=direction, magnitude=int(magnitude))

print(sub.distance * sub.depth)
