import math

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length, min_length = -math.inf, -math.inf
        increasing_array = []

        if nums:
            increasing_array.append(0)
            for i in range(1, len(nums)):
                increasing_array.append(nums[i] - nums[i - 1])

            max_len = 1
            for i in range(1, len(increasing_array)):
                if increasing_array[i] > 0:
                    max_len += 1
                else:
                    max_length = max(max_len, max_length)
                    max_len = 1
            max_length = max(max_len, max_length)

            min_len = 1
            for i in range(1, len(increasing_array)):
                if increasing_array[i] < 0:
                    min_len += 1
                else:
                    min_length = max(min_len, min_length)
                    min_len = 1
            min_length = max(min_len, min_length)

        return max(min_length, max_length)
