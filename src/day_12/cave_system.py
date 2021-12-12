from typing import List
import time

from cave import Cave


class CaveSystem:
    def __init__(self):
        self.caves = {}
        self.journeys = []

    def add_cave_link(self, cave_1: Cave, cave_2: Cave):
        # Ensure both caves are connected to each other
        if cave_1.label not in self.caves:
            self.caves[cave_1.label] = cave_1
        if cave_2.label not in self.caves:
            self.caves[cave_2.label] = cave_2
        self.caves[cave_1.label].add_connected_cave(self.caves[cave_2.label])
        self.caves[cave_2.label].add_connected_cave(self.caves[cave_1.label])

    def find_all_routes(self, starting_cave: str, journey: List[str]):
        journey_copy = list(journey)
        journey_copy.append(starting_cave)
        for cave in self.caves[starting_cave].connected_caves:
            if cave.label == "end":
                journey_copy.append("end")
                self.journeys.append(journey_copy)
            if cave.label.isupper() or cave.label not in journey_copy:
                self.find_all_routes(cave.label, journey_copy)
