from dataclasses import dataclass

from basin import Basin

@dataclass
class HeightPoint():
    height: int
    low_point: bool = False
    basin: Basin = None

    @property
    def risk_level(self):
        return self.height + 1 if self.low_point else 0
