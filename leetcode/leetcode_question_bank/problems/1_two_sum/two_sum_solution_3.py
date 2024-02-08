"""
Title:  1.  Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:
1) 2 <= nums.length <= 10^4
2) -10^9 <= nums[i] <= 10^9
3) -10^9 <= target <= 10^9
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums:
            sorted_nums = sorted(nums)

            low, high = 0, len(nums) - 1
            indices = []

            while low < high:
                if sorted_nums[low] + sorted_nums[high] == target:
                    indices.append(sorted_nums[low])
                    indices.append(sorted_nums[high])
                    break
                elif sorted_nums[low] + sorted_nums[high] < target:
                    low += 1
                else:
                    high -= 1

            if len(indices) == 0:
                return [-1, -1]

            result = []

            for i in range(len(nums)):
                if nums[i] == indices[0]:
                    result.append(i)

            for i in range(len(nums)):
                if nums[i] == indices[1] and i not in result:
                    result.append(i)

            if len(result) == 2:
                return result
            else:
                return [-1, -1]
        return [-1, -1]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.twoSum([2,7,11,15], 9), [0,1])
    test(solution.twoSum([3,2,4], 6), [1,2])
    test(solution.twoSum([3,3], 6), [0,1])
    test(solution.twoSum([], 4), [-1,-1])
    test(solution.twoSum([10, 8, 4], 200), [-1,-1])
