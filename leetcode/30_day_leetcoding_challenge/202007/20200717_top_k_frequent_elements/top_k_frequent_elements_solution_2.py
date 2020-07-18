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
        num_freq_map, min_heap = {}, []

        for num in nums:
            num_freq_map[num] =  num_freq_map.get(num, 0) + 1

        for key, value in num_freq_map.items():
            heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heappop(min_heap)

        return [g[1] for g in min_heap]


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
