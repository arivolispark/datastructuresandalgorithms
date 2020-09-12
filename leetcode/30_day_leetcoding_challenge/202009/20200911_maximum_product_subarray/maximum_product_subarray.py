"""
Title:  Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an
array (containing at least one number) which has the largest product.



Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.



Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""


from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        current_max_product = nums[0]
        prev_max_product = nums[0]
        prev_min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            current_max_product = max(prev_max_product * nums[i], prev_min_product * nums[i], nums[i])
            current_min_product = min(prev_max_product * nums[i], prev_min_product * nums[i], nums[i])
            result = max(result, current_max_product)
            prev_max_product = current_max_product
            prev_min_product = current_min_product
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxProduct([2,3,-2,4]), 6)
    test(solution.maxProduct([-2,0,-1]), 0)
    test(solution.maxProduct([-2,3,-4]), 24)
    test(solution.maxProduct([-2,3,4]), 12)
    test(solution.maxProduct([0,2]), 2)
    test(solution.maxProduct([-3,0,1,-2]), 1)
    test(solution.maxProduct([2,-5,-2,-4,3]), 24)
