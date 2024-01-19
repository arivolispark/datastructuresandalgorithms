from typing import List
import math

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums:
            result = []
            low, high = math.inf, -math.inf
            sorted_nums = sorted(nums)
            start, end = 0, len(sorted_nums) - 1

            while start < end:
                if sorted_nums[start] + sorted_nums[end] < target:
                    start += 1
                elif sorted_nums[start] + sorted_nums[end] > target:
                    end -= 1
                elif sorted_nums[start] + sorted_nums[end] == target:
                    low = min(low, sorted_nums[start])
                    high = max(high, sorted_nums[end])
                    break
            
            for i in range(len(nums)):
                if nums[i] == low:
                    result.append(i)
            for i in range(len(nums)):
                if nums[i] == high and i not in result:
                    result.append(i)

            if len(result) == 2:
                return result
            else:
                return [-1, -1]
        return [-1, -1]
