class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = 0
        nums.append(nums[0])
        for i in range(1, len(nums)):
            result = max(abs(nums[i] - nums[i - 1]), result)
        return result
