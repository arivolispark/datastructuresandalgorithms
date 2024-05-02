class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        map = {}
        if nums:
            for i in range(len(nums)):
                map[nums[i]] = nums[i]
            
            nums.sort()

            for i in range(len(nums), -1, -1):
                if nums[i-1] > 0:
                    if -(nums[i-1]) in map:
                        return nums[i-1]

            return -1
