class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1_map, row2_map, row3_map = {}, {}, {}
        result = []

        row1_map["Q"] = "Q"
        row1_map["W"] = "W"
        row1_map["E"] = "E"
        row1_map["R"] = "R"
        row1_map["T"] = "T"
        row1_map["Y"] = "Y"
        row1_map["U"] = "U"
        row1_map["I"] = "I"
        row1_map["O"] = "O"
        row1_map["P"] = "P"
        row1_map["q"] = "q"
        row1_map["w"] = "w"
        row1_map["e"] = "e"
        row1_map["r"] = "r"
        row1_map["t"] = "t"
        row1_map["y"] = "y"
        row1_map["u"] = "u"
        row1_map["i"] = "i"
        row1_map["o"] = "o"
        row1_map["p"] = "p"

        row2_map["A"] = "A"
        row2_map["S"] = "S"
        row2_map["D"] = "D"
        row2_map["F"] = "F"
        row2_map["G"] = "G"
        row2_map["H"] = "H"
        row2_map["J"] = "J"
        row2_map["K"] = "K"
        row2_map["L"] = "L"
        row2_map["a"] = "a"
        row2_map["s"] = "s"
        row2_map["d"] = "d"
        row2_map["f"] = "f"
        row2_map["g"] = "g"
        row2_map["h"] = "h"
        row2_map["j"] = "j"
        row2_map["k"] = "k"
        row2_map["l"] = "l"

        row3_map["Z"] = "Z"
        row3_map["X"] = "X"
        row3_map["C"] = "C"
        row3_map["V"] = "V"
        row3_map["B"] = "B"
        row3_map["N"] = "N"
        row3_map["M"] = "M"
        row3_map["z"] = "z"
        row3_map["x"] = "x"
        row3_map["c"] = "c"
        row3_map["v"] = "v"
        row3_map["b"] = "b"
        row3_map["n"] = "n"
        row3_map["m"] = "m"

        if words:
            for i in range(len(words)):
                word = words[i]
                match_flag = False

                for c in word:
                    if c in row1_map and is_matching_row(word, row1_map) == True:
                        match_flag = True
                    elif c in row2_map and is_matching_row(word, row2_map) == True:
                        match_flag = True
                    elif c in row3_map and is_matching_row(word, row3_map) == True:
                        match_flag = True
                      
                if match_flag == True:
                    result.append(word)
        return result
        

def is_matching_row(word: str, map: dict) -> bool:
    for c in word:
        if c not in map:
            return False
    return True
