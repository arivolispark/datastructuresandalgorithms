"""
Title:  1780. Check if Number is a Sum of Powers of Three

Given an integer n, return true if it is possible to represent n as the sum of
distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.



Example 1:
Input: n = 12
Output: true
Explanation: 12 = 31 + 32


Example 2:
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34


Example 3:
Input: n = 21
Output: false


Constraints:
1) 1 <= n <= 10^7

"""

from typing import List


class Solution:

    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            n, r = divmod(n, 3)
            if r == 2:
                return False
        return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.checkPowersOfThree(12), True)
    test(solution.checkPowersOfThree(91), True)
    test(solution.checkPowersOfThree(21), False)
