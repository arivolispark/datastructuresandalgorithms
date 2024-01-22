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
            for i in range(0, length):
                result += map[s[i]]

            for i in range(0, length - 1):
                if s[i] == "I" and i + 1 <= length:
                    if s[i + 1] == "V" or s[i + 1] == "X":
                        result -= 2 * map["I"]
                elif s[i] == "X" and i + 1 <= length:
                    if s[i + 1] == "L" or s[i + 1] == "C":
                        result -= 2 * map["X"]
                elif s[i] == "C" and i + 1 <= length:
                    if s[i + 1] == "D" or s[i + 1] == "M":
                        result -= 2 * map["C"]
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
