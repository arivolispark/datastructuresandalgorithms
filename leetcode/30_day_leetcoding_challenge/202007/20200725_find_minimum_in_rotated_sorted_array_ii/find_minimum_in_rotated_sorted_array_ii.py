"""
Title:  Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some
pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1


Example 2:
Input: [2,2,2,0,1]
Output: 0


Note:
1) This is a follow up problem to Find Minimum in Rotated Sorted Array.
2) Would allow duplicates affect the run-time complexity? How and why?

"""

from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        if nums:
            start, end = 0, len(nums) - 1

            while start <= end:
                while nums[start] == nums[end] and start != end:
                    start += 1

                if nums[start] <= nums[end]:
                    return nums[start]

                mid = (start + end) // 2
                if nums[mid] >= nums[start]:
                    start = mid + 1
                else:
                    end = mid
        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findMin([1,3,5]), 1)
    test(solution.findMin([2,2,2,0,1]), 0)
    test(solution.findMin([4,5,6,7,0,1,2]), 0)
