class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = 0
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                delta = nums[i] - nums[i + 1]
                nums[i + 1] += delta + 1
                count += delta + 1 
        return count
