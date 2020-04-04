from typing import List
import math


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        return get_max_subarray_sum(nums, 0, len(nums) - 1)


def get_max_subarray_sum(nums, start, end):
    if start == end:
        return nums[start]

    mid = (start + end) // 2

    max_sum_left_subarray = get_max_subarray_sum(nums, start, mid)
    max_sum_right_subarray = get_max_subarray_sum(nums, mid + 1, end)
    max_sum_crossing_subarray = get_max_crossing_subarray_sum(nums, start, mid, end)

    return max(max_sum_left_subarray, max_sum_crossing_subarray, max_sum_right_subarray)


def get_max_crossing_subarray_sum(nums, start, mid, end):
    max_left_subarray_sum = -math.inf
    current_sum = 0

    for i in range(mid, start - 1, -1):
        current_sum += nums[i]
        max_left_subarray_sum = max(current_sum, max_left_subarray_sum)

    max_right_subarray_sum = -math.inf
    current_sum = 0

    for i in range(mid + 1, end + 1):
        current_sum += nums[i]
        max_right_subarray_sum = max(current_sum, max_right_subarray_sum)

    return max_left_subarray_sum + max_right_subarray_sum


if __name__ == "__main__":
    #nums = [-2]
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    #nums = [-2, 1, -3, 44]
    #nums = [1, 2, 3, 4, 5]
    #nums = [-1, -2]
    print("\n nums: ", nums)

    solution = Solution()
    max_subarray_sum = solution.maxSubArray(nums)
    print("\n max_subarray_sum: ", max_subarray_sum)
