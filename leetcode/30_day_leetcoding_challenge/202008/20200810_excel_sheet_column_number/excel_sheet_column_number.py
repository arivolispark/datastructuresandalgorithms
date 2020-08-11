"""
Title:  Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:


    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...


Example 1:
Input: "A"
Output: 1


Example 2:
Input: "AB"
Output: 28


Example 3:
Input: "ZY"
Output: 701


Constraints:
1) 1 <= s.length <= 7
2) s consists only of uppercase English letters.
3) s is between "A" and "FXSHRXW".


"""


class Solution:

    def titleToNumber(self, s: str) -> int:
        result = 0
        number_of_alphabets = 26
        for i in range(len(s)):
            result *= number_of_alphabets
            result += ord(s[i]) - ord('A') + 1
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.titleToNumber("A"), 1)
    test(solution.titleToNumber("AB"), 28)
    test(solution.titleToNumber("ZY"), 701)
    test(solution.titleToNumber("AAA"), 703)
