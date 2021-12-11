from dataclasses import dataclass



@dataclass
class ChunkCharacter:
    opener: str
    closer: str
    corrupt_points: int
    
    count: str = 0

    def increment(self):
        self.count += 1
