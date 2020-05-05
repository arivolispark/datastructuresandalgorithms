"""
Title:  Number Complement

Given a positive integer, output its complement number. The complement
strategy is to flip the bits of its binary representation.


Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.


Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


Note:
1) The given integer is guaranteed to fit within the range of a 32-bit signed integer.
2) You could assume no leading zero bit in the integer’s binary representation.
3) This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""


class Solution:

    def findComplement(self, num: int) -> int:
        x = num
        number_of_right_shifts = 0
        while x > 0:
            x >>= 1
            number_of_right_shifts += 1

        mask = 1
        val = 1
        for i in range(1, number_of_right_shifts):
            val <<= 1
            mask |= val

        return num ^ mask


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findComplement(5), 2)
    test(solution.findComplement(1), 0)
    test(solution.findComplement(7), 0)
    test(solution.findComplement(10), 5)

