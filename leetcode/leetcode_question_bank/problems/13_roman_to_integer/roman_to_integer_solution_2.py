class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        if s is None:
            return 0
        else:
            result = 0
            length = len(s)

            start = 0
            while start < length:
                result += map[s[start]]

                if s[start] == "I" and start + 1 < length:
                    if s[start + 1] == "V" or s[start + 1] == "X":
                        result -= 2 * map["I"]
                elif s[start] == "X" and start + 1 < length:
                    if s[start + 1] == "L" or s[start + 1] == "C":
                        result -= 2 * map["X"]
                elif s[start] == "C" and start + 1 < length:
                    if s[start + 1] == "D" or s[start + 1] == "M":
                        result -= 2 * map["C"]
                start += 1

            if start == length - 1:
                result += map[s[start + 1]]

            return result
            

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.romanToInt(""), 0)
    test(solution.romanToInt("III"), 3)
    test(solution.romanToInt("LVIII"), 58)
    test(solution.romanToInt("MCMXCIV"), 1994)
