"""
Title:  273. Integer to English Words

Convert a non-negative integer num to its English words representation.



Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"


Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"


Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Constraints:
1) 0 <= num <= 231 - 1

"""

from typing import List


class Solution:

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        less_than_twenty_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        twenty_to_ninety_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        def helper(num: int) -> str:
            if num < 20:
                s = less_than_twenty_map[num]
            elif num < 100:
                s = twenty_to_ninety_map[(num // 10) * 10] + " " + less_than_twenty_map[num % 10]
            elif num < 1000:
                s = helper(num // 100) + " Hundred " + helper(num % 100)
            elif num < 1000000:
                s = helper(num // 1000) + " Thousand " + helper(num % 1000)
            elif num < 1000000000:
                s = helper(num // 1000000) + " Million " + helper(num % 1000000)
            else:
                s = helper(num // 1000000000) + " Billion " + helper(num % 1000000000)

            return s.strip()

        return helper(num)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.numberToWords(0), "Zero")
    test(solution.numberToWords(17), "Seventeen")
    test(solution.numberToWords(91), "Ninety One")
    test(solution.numberToWords(123), "One Hundred Twenty Three")
    test(solution.numberToWords(857), "Eight Hundred Fifty Seven")
    test(solution.numberToWords(12345), "Twelve Thousand Three Hundred Forty Five")
    test(solution.numberToWords(1234567), "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
