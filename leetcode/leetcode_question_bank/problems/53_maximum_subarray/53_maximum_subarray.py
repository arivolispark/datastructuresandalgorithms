"""
Title:  53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.


Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.


Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:
1) 1 <= nums.length <= 10^5
2) -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.

"""


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        local_max = global_max = nums[0]

        for i in range(1, len(nums)):
            local_max = max(nums[i], local_max + nums[i])

            if local_max > global_max:
                global_max = local_max

        return global_max


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
    test(solution.maxSubArray([1]), 1)
    test(solution.maxSubArray([5,4,-1,7,8]), 23)
