"""
Title:  Plus One

Given a non-empty array of digits representing a non-negative integer, plus
one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the
number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.


Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""

from typing import List
from collections import *


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        result = deque()
        if digits:
            size = len(digits)
            remainder = 0
            for i in range(size - 1, -1, -1):
                plus_one_digit = remainder + digits[i]
                if i == size - 1:
                    plus_one_digit += 1
                if plus_one_digit > 9:
                    result.appendleft(0)
                    remainder = 1
                else:
                    result.appendleft(plus_one_digit)
                    remainder = 0
            if remainder == 1:
                result.appendleft(remainder)
        return list(result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.plusOne([1,2,3]), [1,2,4])
    test(solution.plusOne([4,3,2,1]), [4,3,2,2])

    test(solution.plusOne([0]), [1])
    test(solution.plusOne([1]), [2])
    test(solution.plusOne([2]), [3])
    test(solution.plusOne([3]), [4])
    test(solution.plusOne([4]), [5])
    test(solution.plusOne([5]), [6])
    test(solution.plusOne([6]), [7])
    test(solution.plusOne([7]), [8])
    test(solution.plusOne([8]), [9])
    test(solution.plusOne([9]), [1,0])

    test(solution.plusOne([1,0]), [1,1])
    test(solution.plusOne([1,1]), [1,2])
    test(solution.plusOne([1,2]), [1,3])
    test(solution.plusOne([1,3]), [1,4])
    test(solution.plusOne([1,4]), [1,5])
    test(solution.plusOne([1,5]), [1,6])
    test(solution.plusOne([1,6]), [1,7])
    test(solution.plusOne([1,7]), [1,8])
    test(solution.plusOne([1,8]), [1,9])
    test(solution.plusOne([1,9]), [2,0])

    test(solution.plusOne([2,0]), [2,1])
    test(solution.plusOne([2,1]), [2,2])
    test(solution.plusOne([2,2]), [2,3])
    test(solution.plusOne([2,3]), [2,4])
    test(solution.plusOne([2,4]), [2,5])
    test(solution.plusOne([2,5]), [2,6])
    test(solution.plusOne([2,6]), [2,7])
    test(solution.plusOne([2,7]), [2,8])
    test(solution.plusOne([2,8]), [2,9])
    test(solution.plusOne([2,9]), [3,0])

    test(solution.plusOne([8,9]), [9,0])

    test(solution.plusOne([9,0]), [9,1])
    test(solution.plusOne([9,1]), [9,2])
    test(solution.plusOne([9,2]), [9,3])
    test(solution.plusOne([9,3]), [9,4])
    test(solution.plusOne([9,4]), [9,5])
    test(solution.plusOne([9,5]), [9,6])
    test(solution.plusOne([9,6]), [9,7])
    test(solution.plusOne([9,7]), [9,8])
    test(solution.plusOne([9,8]), [9,9])
    test(solution.plusOne([9,9]), [1,0,0])

    test(solution.plusOne([9,8,9]), [9,9,0])
    test(solution.plusOne([9,9,0]), [9,9,1])
    test(solution.plusOne([9,9,1]), [9,9,2])
    test(solution.plusOne([9,9,2]), [9,9,3])
    test(solution.plusOne([9,9,3]), [9,9,4])
    test(solution.plusOne([9,9,4]), [9,9,5])
    test(solution.plusOne([9,9,5]), [9,9,6])
    test(solution.plusOne([9,9,6]), [9,9,7])
    test(solution.plusOne([9,9,7]), [9,9,8])

    test(solution.plusOne([9,9,8]), [9,9,9])
    test(solution.plusOne([9,9,9]), [1,0,0,0])
    test(solution.plusOne([1,0,0,0]), [1,0,0,1])
