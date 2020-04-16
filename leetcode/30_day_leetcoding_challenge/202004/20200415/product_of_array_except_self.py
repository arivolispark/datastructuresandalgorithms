"""
Title:  Product of Array Except Self

Given an array nums of n integers where n > 1,  return an
array output such that output[i] is equal to the
product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any
prefix or suffix of the array (including the whole array) fits
in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output
array does not count as extra space for the purpose of space
complexity analysis.)
"""

from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return [0]

        product = []

        left = [0] * n
        right = [0] * n

        left[0] = 1
        right[n - 1] = 1

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            product.append(left[i] * right[i])

        return product


def get_test_case_1():
    return None


def get_test_case_2():
    return []


def get_test_case_3():
    nums = [1, 2, 3, 4]
    return nums


def get_test_case_4() -> List[int]:
    nums = [0, 0]
    return nums


def get_test_case_5() -> List[int]:
    nums = [1, 0]
    return nums


if __name__ == "__main__":
    solution = Solution()

    #nums = get_test_case_1()
    #nums = get_test_case_2()
    nums = get_test_case_3()
    #nums = get_test_case_4()
    #nums = get_test_case_5()

    print("\n nums: ", nums)

    result = solution.productExceptSelf(nums)
    print("\n\n result: ", result)
