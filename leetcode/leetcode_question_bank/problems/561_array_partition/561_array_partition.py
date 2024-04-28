class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        if nums:
            nums.sort()
            for i in range(0, len(nums), 2):
                result += nums[i]
        return result
