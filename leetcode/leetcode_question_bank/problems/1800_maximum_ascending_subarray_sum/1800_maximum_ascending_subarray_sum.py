class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = []
        length = len(nums)

        for i in range(length):
            result.append(nums[i]) 
        
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                result[i] += result[i - 1]

        return max(result)
