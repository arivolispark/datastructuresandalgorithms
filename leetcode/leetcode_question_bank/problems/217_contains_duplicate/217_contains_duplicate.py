"""
Title:  217. Contains Duplicate


Given an integer array nums, return true if any value appears at least twice in the array, and return
false if every element is distinct.


Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:
1) 1 <= nums.length <= 10^5
1) -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums:
            map = {}
            for i in range(len(nums)):
                if nums[i] in map:
                    return True
                map[nums[i]] = nums[i]
        return False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.containsDuplicate([1,2,3,1]), True)
    test(solution.containsDuplicate([1,2,3,4]), False)
    test(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)
