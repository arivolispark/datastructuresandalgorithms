"""
Title:  Subsets

Given a set of distinct integers, nums, return all possible
subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        if nums:
            subsets.append([])

            for num in nums:
                size = len(subsets)
                for i in range(size):
                    set = list(subsets[i])
                    set.append(num)
                    subsets.append(set)
        return subsets


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.subsets([]), [])
    test(solution.subsets([1]), [[],[1]])
    test(solution.subsets([1,2]), [[],[1],[2],[1,2]])
    test(solution.subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
