"""
Title:  78. Subsets

Given an integer array nums of unique elements, return all
possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the
solution in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


Example 2:
Input: nums = [0]
Output: [[],[0]]


Constraints:
1) 1 <= nums.length <= 10
2) -10 <= nums[i] <= 10
3) All the numbers of nums are unique.

"""

from typing import List
import itertools


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])
        for i in range(len(nums)):
            result += itertools.combinations(nums, i + 1)
        result = [ list(t) for t in result ]
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
    test(solution.subsets([0]), [[],[0]])
