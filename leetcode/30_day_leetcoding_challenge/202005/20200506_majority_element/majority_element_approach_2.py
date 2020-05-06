"""
Title:  Majority Element

Given an array of size n, find the majority element. The majority
element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element
always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3


Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

"""

from typing import List
from collections import deque


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque()

        for i in range(n):
            if len(q) == 0:
                q.append(nums[i])
            else:
                if q[-1] != nums[i]:
                    q.pop()
                else:
                    q.append(nums[i])
        return q.pop()


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.majorityElement([3, 2, 3]), 3)
    test(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
