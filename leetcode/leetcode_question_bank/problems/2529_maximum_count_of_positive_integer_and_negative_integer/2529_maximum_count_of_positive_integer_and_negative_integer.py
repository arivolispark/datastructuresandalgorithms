import math

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_of_positive, count_of_negative = 0, 0
        if nums:
            for i in range(len(nums)):
                if nums[i] > 0:
                    count_of_positive += 1
                elif nums[i] < 0:
                    count_of_negative += 1
        
        return max(count_of_positive, count_of_negative)
