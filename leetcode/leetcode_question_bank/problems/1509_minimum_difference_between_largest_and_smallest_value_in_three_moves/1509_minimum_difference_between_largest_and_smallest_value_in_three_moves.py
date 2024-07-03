class Solution:
    def minDifference(self, nums: List[int]) -> int:
        result = 0

        length = len(nums)
        if length < 5:
            return 0

        result = math.inf

        nums.sort()

        for i in range(4):
            result = min(result, nums[length - 4 + i] - nums[i])

        return result
