"""
Title:  896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An
array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.



Example 1:
Input: nums = [1,2,2,3]
Output: true


Example 2:
Input: nums = [6,5,4,4]
Output: true


Example 3:
Input: nums = [1,3,2]
Output: false


Constraints:
1) 1 <= nums.length <= 10^5
2) -10^5 <= nums[i] <= 10^5

"""

from typing import List


class Solution:

    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = None, None
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] > nums[i - 1]:
                increasing = True
            elif nums[i] < nums[i - 1]:
                decreasing = True

            if increasing is not None and decreasing is not None:
                if increasing == True and decreasing == True:
                    return False
        return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.isMonotonic([1,2,2,3]), True)
    test(solution.isMonotonic([6,5,4,4]), True)
    test(solution.isMonotonic([1,3,2]), False)
    test(solution.isMonotonic([-101,0,3,2]), False)
    test(solution.isMonotonic([-101,0,3,200]), True)
