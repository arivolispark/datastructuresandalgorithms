"""
Title:  Single Number III

Given an array of numbers nums, in which exactly two elements appear only
once and all the other elements appear exactly twice. Find the two elements
that appear only once.


Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]


Note:
1) The order of the result is not important. So in the above
example, [5, 3] is also correct.
2) Your algorithm should run in linear runtime complexity. Could
you implement it using only constant space complexity?

"""

from typing import List


class Solution:

    def singleNumber(self, nums: List[int]):
        ans = 0
        for num in nums:
            ans ^= num

        ans &= -ans
        res = [0] * 2

        for num in nums:
            if ans & num:
                res[0] ^= num
            else:
                res[1] ^= num
        return res


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.singleNumber([1,2,1,3,2,5]), [3,5])
