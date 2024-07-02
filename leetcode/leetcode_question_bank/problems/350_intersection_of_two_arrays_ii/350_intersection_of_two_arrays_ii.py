"""
Title:  350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must appear as many times
as it shows in both arrays and you may return the result in any order.


Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]


Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:
1) 1 <= nums1.length, nums2.length <= 1000
2) 0 <= nums1[i], nums2[i] <= 1000


Follow up:
1) What if the given array is already sorted? How would you optimize your algorithm?
2) What if nums1's size is small compared to nums2's size? Which algorithm is better?
3) What if elements of nums2 are stored on disk, and the memory is limited such that you
cannot load all elements into the memory at once?

"""

import math
from typing import List

class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        map_1, map_2 = {}, {}

        for i in range(len(nums1)):
            map_1[nums1[i]] = map_1.get(nums1[i], 0) + 1

        for i in range(len(nums2)):
            map_2[nums2[i]] = map_2.get(nums2[i], 0) + 1

        for k1, v1 in map_1.items():
            if k1 in map_2:
                v2 = map_2[k1]
                for i in range(min(v1, v2)):
                    result.append(k1)

        return result

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.intersect([1,2,2,1], [2,2]), [2,2])
    test(solution.intersect([4,9,5], [9,4,9,8,4]), [4,9])
