"""
Problem #: 7
Title:  Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.


Example 1:
Input: 123
Output: 321


Example 2:
Input: -123
Output: -321


Example 3:
Input: 120
Output: 21


Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.

"""


class Solution:

    def reverse(self, x: int) -> int:
        reversed_integer = 0
        negative = False

        if x < 0:
            negative = True
            x = abs(x)

        while x > 0:
            reversed_integer = reversed_integer * 10 + (x % 10)
            x //= 10

        if negative:
            reversed_integer = -reversed_integer

        if reversed_integer >= 2147483647 or reversed_integer <= -2147483648:
            #print("WARNING: Number overflow encountered!")
            reversed_integer = 0

        return reversed_integer


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.reverse(123), 321)
    test(solution.reverse(-123), -321)
    test(solution.reverse(120), 21)
    test(solution.reverse(1534236469), 0)
    test(solution.reverse(-2147483648), 0)
