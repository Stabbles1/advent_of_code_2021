from dataclasses import dataclass

from chunk_character import ChunkCharacter


@dataclass
class ChunkLine:
    line: str
    corrupt_character: str = ""
    closing_characters = {")": "(", "]": "[", "}": "{", ">": "<"}
    opening_characters = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": 1, "]": 2, "}": 3, ">": 4}

    def is_corrupt(self) -> bool:
        current_chain = ""
        for char in self.line:
            if char not in self.closing_characters:
                current_chain += char
            else:
                if self.closing_characters[char] != current_chain[-1]:
                    self.corrupt_character = char
                    return True
                else:
                    current_chain = current_chain[0:-1]
        return False

    def get_completion_sequence(self) -> str:
        current_chain = ""
        for char in self.line:
            if char not in self.closing_characters:
                current_chain += char
            else:
                current_chain = current_chain[0:-1]
        return "".join([self.opening_characters[char] for char in current_chain[::-1]])

    def completion_score(self) -> int:
        total = 0
        for char in self.get_completion_sequence():
            total *= 5
            total += self.scores[char]
        return total
