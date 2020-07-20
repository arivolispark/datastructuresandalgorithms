"""
Title:  Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"


Example 2:
Input: a = "1010", b = "1011"
Output: "10101"


Constraints:
1) Each string consists only of '0' or '1' characters.
2) 1 <= a.length, b.length <= 10^4
3) Each string is either "0" or doesn't contain any leading zero

"""


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        result = ""

        if a and b:
            a_len, b_len = len(a) - 1, len(b) - 1
            remainder = 0
            i, j = a_len, b_len
            if a_len >= b_len:
                while i > -1 and j > -1:
                    sum = remainder + int(a[i]) + int(b[j])
                    sum, remainder = calculate_sum_and_remainder(sum)

                    result += str(sum)
                    i -= 1
                    j -= 1
                while i > -1:
                    sum = remainder + int(a[i])
                    sum, remainder = calculate_sum_and_remainder(sum)

                    result += str(sum)
                    i -= 1
                if remainder == 1:
                    result += str(1)
            elif b_len >= a_len:
                while i > -1 and j > -1:
                    sum = remainder + int(a[i]) + int(b[j])
                    sum, remainder = calculate_sum_and_remainder(sum)

                    result += str(sum)
                    i -= 1
                    j -= 1
                while j > -1:
                    sum = remainder + int(b[j])
                    sum, remainder = calculate_sum_and_remainder(sum)

                    result += str(sum)
                    j -= 1
                if remainder == 1:
                    result += str(1)

        return result[::-1]


def calculate_sum_and_remainder(sum: int) -> (int, int):
    if sum == 2:
        sum = 0
        remainder = 1
    elif sum == 3:
        sum = 1
        remainder = 1
    else:
        remainder = 0
    return sum, remainder


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.addBinary("11", "1"), "100")
    test(solution.addBinary("1010", "1011"), "10101")
    test(solution.addBinary("1", "111"), "1000")
    test(solution.addBinary("100", "110010"), "110110")
    test(solution.addBinary("100", "110010"), "110110")
    test(solution.addBinary("101111", "10"), "110001")
    test(solution.addBinary("110010", "10111"), "1001001")
    test(solution.addBinary("1111", "1111"), "11110")
