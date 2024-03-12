"""
Title:  Sort a list of positive integers in descending order after removing duplicates


Example 1:
Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


Example 2:
Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


Example 3:
Input: nums = [10, 1, 4, 3, 8, 7, 6, 9, 5, 2]
Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



Constraints:
1) 1 <= nums.length <= 10^4
2) -2^31 <= nums[i] <= 2^31 - 1


Follow up: Can you find an O(n) solution?
"""


from typing import List
from heapq import *


class Solution:

    def descending_sort(self, nums: List[int]) -> List[int]:
        dict = {}
        max_heap = []
        result = []

        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = nums[i]
                heappush(max_heap, -nums[i])

        while max_heap:
            result.append(-heappop(max_heap))

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.descending_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    test(solution.descending_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    test(solution.descending_sort([10, 1, 4, 3, 8, 7, 6, 9, 5, 2]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
