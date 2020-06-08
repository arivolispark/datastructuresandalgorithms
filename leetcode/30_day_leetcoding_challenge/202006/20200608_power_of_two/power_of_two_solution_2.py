"""
Title:  Power of Two

Given an integer, write a function to determine
if it is a power of two.



Example 1:
Input: 1
Output: true
Explanation: 2^0 = 1


Example 2:
Input: 16
Output: true
Explanation: 2^4 = 16


Example 3:
Input: 218
Output: false

"""


class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        return True if n > 0 and (n & (n - 1) == 0) else False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.isPowerOfTwo(1), True)
    test(solution.isPowerOfTwo(16), True)
    test(solution.isPowerOfTwo(218), False)
