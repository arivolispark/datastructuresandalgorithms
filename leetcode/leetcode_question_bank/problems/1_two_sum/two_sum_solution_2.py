import math

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        if nums:
            low, high = math.inf, -math.inf
            sorted_nums = sorted(nums)
            start, end = 0, len(sorted_nums) - 1

            while start <= end:
                if sorted_nums[start] + sorted_nums[end] < target:
                    start = start + 1
                elif sorted_nums[start] + sorted_nums[end] > target:
                    end = end - 1
                elif sorted_nums[start] + sorted_nums[end] == target:
                    low = min(low, sorted_nums[start])
                    high = max(high, sorted_nums[end])
                    break
            
            for i in range(len(nums)):
                if nums[i] == low and i not in result:
                    result.append(i)
                if nums[i] == high and i not in result:
                    result.append(i)

        return result
