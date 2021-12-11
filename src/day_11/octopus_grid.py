from typing import List
import itertools

from octopus import Octopus

class OctopusGrid:

    def __init__(self, grid: List[List[Octopus]]):
        self.grid = grid

    def increase_all_energy_levels(self):
        for row in self.grid:
            for octopus in row:
                octopus.increase_energy()

    def start_flashing(self):
        new_octopus_flash = True
        flash_count = 0
        while new_octopus_flash:
            new_octopus_flash = False
            for row_index, row in enumerate(self.grid):
                for col_index, octopus in enumerate(row):
                    if octopus.flashing and not octopus.energy_sent:
                        self.energise_surrounding_octopus(row_index, col_index)
                        octopus.energy_sent = True
                        flash_count += 1
                        new_octopus_flash = True
        return flash_count

    def energise_surrounding_octopus(self, row_index, col_index):
        for row_offset, col_offset in list(itertools.product([-1, 0, 1], [-1, 0, 1])):
            try:
                if row_index + row_offset >= 0 and col_index + col_offset >= 0:
                    self.grid[row_index + row_offset][col_index + col_offset].increase_energy()
            except IndexError:
                pass # There wasn't an octopus there

    def stop_flashing(self):
        for row in self.grid:
            for octopus in row:
                octopus.stop_flashing()

    def print_grid(self):
        for row in self.grid:
            print(str(row))

    def run_steps(self, steps=1):
        total_flash_count = 0
        for _ in range(steps):
            self.increase_all_energy_levels()
            total_flash_count += self.start_flashing()
            self.stop_flashing()
        return total_flash_count
