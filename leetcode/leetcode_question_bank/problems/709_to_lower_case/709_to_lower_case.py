class Solution:
    def toLowerCase(self, s: str) -> str:
        char_map = {
            "A": "a",
            "B": "b",
            "C": "c",
            "D": "d",
            "E": "e",
            "F": "f",
            "G": "g",
            "H": "h",
            "I": "i",
            "J": "j",
            "K": "k",
            "L": "l",
            "M": "m",
            "N": "n",
            "O": "o",
            "P": "p",
            "Q": "q",
            "R": "r",
            "S": "s",
            "T": "t",
            "U": "u",
            "V": "v",
            "W": "w",
            "X": "x",
            "Y": "y",
            "Z": "z"
        }

        if s:
            l = list(s)
            for i in range(len(l)):
                if l[i] in char_map:
                   l[i] = char_map[s[i]] 
        return "".join(l)
