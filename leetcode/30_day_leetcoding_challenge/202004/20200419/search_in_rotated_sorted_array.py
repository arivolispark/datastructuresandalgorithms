"""
Title:  Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some
pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array
return its index, otherwise return -1.

You may assume no duplicate exists in the array.  Your algorithm's
runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if nums:
            n = len(nums)

            if n == 1:
                if target == nums[0]:
                    return 0
                else:
                    return -1

            pivot = -1
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    pivot = i
                    break

            if pivot == -1:
                return binary_search(nums, 0, n - 1, target)
            else:
                if nums[0] <= target <= nums[pivot]:
                    return binary_search(nums, 0, pivot, target)
                elif nums[pivot + 1] <= target <= nums[n - 1]:
                    return binary_search(nums, pivot + 1, n - 1, target)
                else:
                    return -1
        return -1


def binary_search(nums: List[int], start: int, end: int, target: int) -> int:
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def get_test_case_1() -> (List[List[int]], int):
    nums = None
    target = 0
    return nums, target


def get_test_case_2() -> (List[List[int]], int):
    nums = []
    target = 0
    return nums, target


def get_test_case_3() -> (List[List[int]], int):
    nums = [4]
    target = 10
    return nums, target


def get_test_case_4() -> (List[List[int]], int):
    nums = [4]
    target = 4
    return nums, target


def get_test_case_5() -> (List[List[int]], int):
    nums = [1, 3]
    target = 0
    return nums, target


def get_test_case_6() -> (List[List[int]], int):
    nums = [1, 3]
    target = 1
    return nums, target


def get_test_case_7() -> (List[List[int]], int):
    nums = [1, 3]
    target = 3
    return nums, target


def get_test_case_8() -> (List[List[int]], int):
    nums = [4, 2]
    target = 10
    return nums, target


def get_test_case_9() -> (List[List[int]], int):
    nums = [4, 2]
    target = 2
    return nums, target


def get_test_case_10() -> (List[List[int]], int):
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    return nums, target


def get_test_case_11() -> (List[List[int]], int):
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    return nums, target


if __name__ == "__main__":
    solution = Solution()

    #nums, target = get_test_case_1()
    #nums, target = get_test_case_2()
    #nums, target = get_test_case_3()
    #nums, target = get_test_case_4()
    #nums, target = get_test_case_5()
    #nums, target = get_test_case_6()
    #nums, target = get_test_case_7()
    #nums, target = get_test_case_8()
    #nums, target = get_test_case_9()
    nums, target = get_test_case_10()
    #nums, target = get_test_case_11()

    print("\n nums: ", nums)
    print(" target: ", target)

    index = solution.search(nums, target)
    print("\n index: ", index)
