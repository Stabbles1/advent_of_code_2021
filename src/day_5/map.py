from typing import List

from vent import Vent

class Map:

    def __init__(self):
        self.vent_locations = {} # Where "1,3" : 2 represents 2 vents at x=1,y=3


    def advent(self, vent: Vent):
        for coordinate in vent.calculate_all_coordinates():
            if coordinate == "0,0":
                print(f"Found him {vent} and his coordinates {vent.calculate_all_coordinates()}")
            if coordinate in self.vent_locations:
                self.vent_locations[coordinate] += 1
            else:
                self.vent_locations[coordinate] = 1

    def dangerous_coordinates(self, danger_threshold):
        return [ k for k, v in self.vent_locations.items() if v >= danger_threshold ]