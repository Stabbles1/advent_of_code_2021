from typing import List
from digit import Digit
from puzzle import Puzzle


class Puzzle2(Puzzle):
    def get_decoded_readings(self) -> int:
        self.run_eliminations()
        decoded_readings = ""
        for digit in self.readings:
            decoded_readings += str((digit.characters_to_int_pt_2(self.possibilities)))
        return int(decoded_readings)

    def eliminate_based_on_length(self):
        length_decoder = {
            2: ["a", "b"],
            3: ["d", "a", "b"],
            4: ["e", "a", "f", "b"],
        }
        for digit in self.clues + self.readings:
            if len(digit) in length_decoder:
                for letter in digit.characters:
                    self.submit_possibilities(letter, length_decoder[len(digit)])
        return

    def eliminate_based_on_commonality(self):
        commonality_decoder = {
            8: ["d", "a"],
            6: ["e"],
            7: ["f", "c"],
            4: ["g"],
            9: ["b"],
        }
        for letter in "abcdefg":
            count = self.raw_clues.count(letter)
            self.submit_possibilities(letter, commonality_decoder[count])
