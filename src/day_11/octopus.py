from dataclasses import dataclass

@dataclass
class Octopus:
    energy_level: int
    flashing: bool = False
    energy_sent: bool = False

    def increase_energy(self):
        if self.energy_level == 9:
            self.flashing = True
        if self.flashing:
            self.energy_level = 0
        else:
            self.energy_level += 1

    def stop_flashing(self):
        self.flashing = False
        self.energy_sent = False

    def __str__(self):
        return f"*{self.energy_level}*" if self.flashing else f" {self.energy_level} "
    
    def __repr__(self):
        return f"*{self.energy_level}*" if self.flashing else f" {self.energy_level} "
