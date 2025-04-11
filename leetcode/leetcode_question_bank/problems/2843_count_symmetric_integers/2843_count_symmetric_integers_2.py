"""
Title:  2843. Count Symmetric Integers

You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum
of the first n digits of x is equal to the sum of the last n digits
of x. Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].



Example 1:
Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.


Example 2:
Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.


Constraints:
1) 1 <= low <= high <= 10^4

"""

from typing import List


class Solution:

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = []

        for i in range(low, high + 1):
            digits = get_digits(i)

            if len(digits) % 2 == 0:
                size = len(digits)
                l_sum, r_sum = 0, 0

                for j in range(size // 2):
                    r_sum += digits[j]
                for j in range((size // 2), size):
                    l_sum += digits[j]

                if l_sum == r_sum:
                    result.append(i)

        return len(result)


def get_digits(num: int) -> List[int]:
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.countSymmetricIntegers(1, 100), 9)
    #test(solution.countSymmetricIntegers(1, 10000), 9)
    test(solution.countSymmetricIntegers(1200, 1230), 4)
