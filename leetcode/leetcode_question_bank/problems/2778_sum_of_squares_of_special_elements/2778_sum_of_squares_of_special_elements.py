class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        if nums:
            n = len(nums)
            for i in range(len(nums)):
                if n % (i + 1) == 0:
                    result += nums[i] * nums[i]
        return result
