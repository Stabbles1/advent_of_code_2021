class Digit:
    
    def __init__(self, characters):
        self.characters = characters

    def __len__(self):
        return len(self.characters)

    def characters_to_int(self, possibilities):
        decoded_characters = "".join([ possibilities[char][0] for char in self.characters ])
        representations = {
            "abcefg" : 0,
            "cf" : 1,
            "acdeg" : 2,
            "acdfg" : 3,
            "bcdf" : 4,
            "abdfg" : 5,
            "abdefg" : 6,
            "acf" : 7,
            "abcdefg" : 8,
            "abcdfg" : 9,

        }
        return representations["".join(sorted(decoded_characters))]
