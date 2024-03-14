"""
Title: 507.  Perfect Number

A perfect number is a positive integer that is equal to the sum of its positive
divisors, excluding the number itself. A divisor of an integer x is an integer
that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.


Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.


Example 2:
Input: num = 7
Output: false


Constraints:
1) 1 <= num <= 10^8

"""

import math


class Solution:

    def checkPerfectNumber(self, num: int) -> bool:
        divisor_set = set()

        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisor_set.add(i)
                divisor_set.add(num // i)

        total = 0
        for divisor in divisor_set:
            total += divisor
        total -= num

        return True if total == num else False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.checkPerfectNumber(28), True)
    test(solution.checkPerfectNumber(7), False)
    test(solution.checkPerfectNumber(99999996), False)
