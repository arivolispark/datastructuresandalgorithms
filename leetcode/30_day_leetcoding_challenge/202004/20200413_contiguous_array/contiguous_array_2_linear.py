"""
Title:  Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.


Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.

"""

from typing import List


class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_contiguous_array_length = 0
        sum_index_map = {}
        curr_sum = 0

        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
            else:
                nums[i] = 1

        for i in range(n):
            curr_sum += nums[i]

            if curr_sum == 0:
                max_contiguous_array_length = i + 1

            if curr_sum not in sum_index_map:
                sum_index_map[curr_sum] = i
            else:
                if max_contiguous_array_length < i - sum_index_map[curr_sum]:
                    max_contiguous_array_length = i - sum_index_map[curr_sum]

        for i in range(n):
            if nums[i] == -1:
                nums[i] = 0
            else:
                nums[i] = 1

        return max_contiguous_array_length


def get_test_case_1() -> List[int]:
    return []


def get_test_case_2() -> List[int]:
    return [0]


def get_test_case_3() -> List[int]:
    return [1]


def get_test_case_4() -> List[int]:
    return [0, 0]


def get_test_case_5() -> List[int]:
    return [1, 1]


def get_test_case_6() -> List[int]:
    return [0, 1, 1, 0, 0, 1, 0, 1, 1, 0]


def get_test_case_7() -> List[int]:
    return [0, 1, 1, 0, 1, 1, 1, 0]


def get_test_case_8() -> List[int]:
    return [0, 1, 0]


def get_test_case_9() -> List[int]:
    return [0, 0, 1, 0, 0, 0, 1, 1]


if __name__ == "__main__":
    solution = Solution()

    #nums = get_test_case_1()
    #nums = get_test_case_2()
    #nums = get_test_case_3()
    #nums = get_test_case_4()
    #nums = get_test_case_5()
    #nums = get_test_case_6()
    #nums = get_test_case_7()
    #nums = get_test_case_8()
    nums = get_test_case_9()
    print("\n nums: ", nums)

    max_contiguous_array_length = solution.findMaxLength(nums)
    print("\n max_contiguous_array_length: ", max_contiguous_array_length)
