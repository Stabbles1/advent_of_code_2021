from dataclasses import dataclass



@dataclass
class ChunkCharacter:
    opener: str
    closer: str
    points: int
