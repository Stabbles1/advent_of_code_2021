from typing import List
from digit import Digit


class Puzzle:
    """ Represents a single line of the input, the left and right
    sides of the puzzle are passed in as separate arguments"""
    def __init__(self, clues, readings):
        self.raw_clues = clues
        self.clues: List[Digit] = [Digit(characters) for characters in clues.split(" ")]
        self.readings: List[Digit] = [Digit(characters) for characters in readings.split(" ")]
        self.possibilities = {
            letter: ["a", "b", "c", "d", "e", "f", "g"] for letter in "abcdefg"
        }

    def get_decoded_readings(self) -> List[int]:
        self.run_eliminations()
        decoded_readings = []
        for digit in self.readings:
            decoded_readings.append(digit.characters_to_int(self.possibilities))
        return decoded_readings

    def get_decoded_readings_pt2(self) -> int:
        self.run_eliminations()
        decoded_readings = ""
        for digit in self.readings:
            decoded_readings += str((digit.characters_to_int_pt_2(self.possibilities)))
        return int(decoded_readings)

    def run_eliminations(self):
        self.eliminate_based_on_length()
        self.eliminate_based_on_commonality()
        self.eliminate_based_on_already_known()

    def eliminate_based_on_length(self):
        length_decoder = {
            2: ["c", "f"],
            3: ["a", "c", "f"],
            4: ["b", "c", "d", "f"],
        }
        for digit in self.clues + self.readings:
            if len(digit) in length_decoder:
                for letter in digit.characters:
                    self.submit_possibilities(letter, length_decoder[len(digit)])
        return


    def eliminate_based_on_commonality(self):
        commonality_decoder = {
            8: ['a', 'c'],
            6: ['b'],
            7: ['d', 'g'],
            4: ['e'],
            9: ['f'],
        }
        for letter in "abcdefg":
            count = self.raw_clues.count(letter)
            self.submit_possibilities(letter, commonality_decoder[count])

    def eliminate_based_on_already_known(self):
        # Wowee I hope no one sees this
        for encoded, decoded in self.possibilities.items():
            if len(decoded) > 1:
                for letter in decoded:
                    for encoded_inner, decoded_inner in self.possibilities.items():
                        if [letter] == decoded_inner:
                            self.possibilities[encoded].remove(decoded_inner[0])


    def submit_possibilities(self, letter: str, options: List[str]):
        for remaining_letters in list(self.possibilities[letter]):
            if remaining_letters not in options:
                self.possibilities[letter].remove(remaining_letters)
