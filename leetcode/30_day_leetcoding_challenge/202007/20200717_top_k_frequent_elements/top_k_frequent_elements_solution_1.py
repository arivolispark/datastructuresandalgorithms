"""
Title:  Top K Frequent Elements)

Given a non-empty array of integers, return the k most frequent elements.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Example 3:
Input: nums = [1], k = 1
Output: [1]


Note:
1) You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
2) Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
3) It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
4) You can return the answer in any order.

"""

from typing import List
from heapq import *


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        if nums:
            number_freq = {}
            for i in range(len(nums)):
                number_freq[nums[i]] = number_freq.get(nums[i], 0) + 1

            max_heap = []
            for key, value in number_freq.items():
                heappush(max_heap, (-value, key))

            for i in range(k):
                freq, num = heappop(max_heap)
                result.append(num)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.topKFrequent([1,1,1,2,2,3], 2), [1,2])
    test(solution.topKFrequent([1], 1), [1])
