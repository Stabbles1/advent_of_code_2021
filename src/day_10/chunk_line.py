from dataclasses import dataclass

from chunk_character import ChunkCharacter


@dataclass
class ChunkLine:
    line: str
    corrupt_character: str = ""
    closing_characters = {
        ")": ChunkCharacter("(", ")", 3),
        "]": ChunkCharacter("[", "]", 57),
        "}": ChunkCharacter("{", "}", 1197),
        ">": ChunkCharacter("<", ">", 25137),
    }

    def is_corrupt(self) -> bool:
        current_chain = ""
        for char in self.line:
            if char not in self.closing_characters:
                current_chain += char
            else:
                if self.closing_characters[char].opener != current_chain[-1]:
                    self.corrupt_character = char
                    return True
                else:
                    current_chain = current_chain[0:-1]
        return False

