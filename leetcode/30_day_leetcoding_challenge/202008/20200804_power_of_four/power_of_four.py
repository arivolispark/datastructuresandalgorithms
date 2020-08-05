"""
Title:  Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:
Input: 16
Output: true


Example 2:
Input: 5
Output: false


Follow up: Could you solve it without loops/recursion?

"""


class Solution:

    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        power_of_two = num & (num - 1) == 0
        four_in_zeroth_place = num % 10 == 4
        six_in_zeroth_place = num % 10 == 6
        return power_of_two and (four_in_zeroth_place or six_in_zeroth_place)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.isPowerOfFour(1), True)
    test(solution.isPowerOfFour(2), False)
    test(solution.isPowerOfFour(3), False)
    test(solution.isPowerOfFour(4), True)
    test(solution.isPowerOfFour(5), False)
    test(solution.isPowerOfFour(6), False)
    test(solution.isPowerOfFour(7), False)
    test(solution.isPowerOfFour(8), False)
    test(solution.isPowerOfFour(9), False)
    test(solution.isPowerOfFour(10), False)
    test(solution.isPowerOfFour(11), False)
    test(solution.isPowerOfFour(12), False)
    test(solution.isPowerOfFour(13), False)
    test(solution.isPowerOfFour(14), False)
    test(solution.isPowerOfFour(15), False)
    test(solution.isPowerOfFour(16), True)
    test(solution.isPowerOfFour(17), False)
    test(solution.isPowerOfFour(18), False)
    test(solution.isPowerOfFour(19), False)
    test(solution.isPowerOfFour(20), False)

    test(solution.isPowerOfFour(27), False)

    test(solution.isPowerOfFour(63), False)
    test(solution.isPowerOfFour(64), True)
    test(solution.isPowerOfFour(65), False)

    test(solution.isPowerOfFour(79), False)
    test(solution.isPowerOfFour(80), False)
    test(solution.isPowerOfFour(81), False)
    test(solution.isPowerOfFour(82), False)
    test(solution.isPowerOfFour(83), False)

    test(solution.isPowerOfFour(255), False)
    test(solution.isPowerOfFour(256), True)
    test(solution.isPowerOfFour(257), False)
    test(solution.isPowerOfFour(258), False)
