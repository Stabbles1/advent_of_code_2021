from dataclasses import dataclass

@dataclass(_cls)
class LetterClue:
    self.encoded: str
    self.decoded: List[str] = field(default_factory=lambda:["a", "b", "c", "d", "e", "f", "g"])

    