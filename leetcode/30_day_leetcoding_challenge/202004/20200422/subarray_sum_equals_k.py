"""
Title:  Subarray Sum Equals K

Given an array of integers and an integer k, you need to find
the total number of continuous subarrays whose sum equals to k.



Example 1:

Input:nums = [1,1,1], k = 2
Output: 2


Note:
1) The length of the array is in range [1, 20,000].
2) The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""

from typing import List


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        sums = {}
        cur_sum = 0
        sums[cur_sum] = 1
        res = 0
        for i in nums:
            cur_sum += i
            if cur_sum - k in sums:
                res += sums[cur_sum - k]
            if cur_sum in sums:
                sums[cur_sum] = sums[cur_sum] + 1
            else:
                sums[cur_sum] = 1
        return res
        """

        count_subarray_sum = 0
        if nums:
            n = len(nums)
            if n > 0:
                previous_sum_map = {}
                current_sum = 0

                for i in range(0, n):
                    current_sum += nums[i]

                    if current_sum == k:
                        count_subarray_sum += 1

                    if (current_sum - k) in previous_sum_map:
                        count_subarray_sum += previous_sum_map[current_sum - k]

                    previous_sum_map[current_sum] = previous_sum_map.get(current_sum, 0) + 1
        return count_subarray_sum


def get_test_case_1() -> (List[int], int):
    nums = [1, 1, 1]
    k = 2
    return nums, k


def get_test_case_2() -> (List[int], int):
    nums = [1, 2, 3]
    k = 3
    return nums, k


def get_test_case_3() -> (List[int], int):
    nums = [1]
    k = 0
    return nums, k


def get_test_case_4() -> (List[int], int):
    nums = [-1, -1, 1]
    k = 0
    return nums, k


def get_test_case_5() -> (List[int], int):
    nums = [100, 1, 2, 3]
    k = 6
    return nums, k


if __name__ == "__main__":
    solution = Solution()

    #nums, k = get_test_case_1()
    #nums, k = get_test_case_2()
    nums, k = get_test_case_3()
    #nums, k = get_test_case_4()
    nums, k = get_test_case_5()
    print("\n nums: ", nums)
    print(" k: ", k)

    result = solution.subarraySum(nums, k)
    print("\n result: ", result)
