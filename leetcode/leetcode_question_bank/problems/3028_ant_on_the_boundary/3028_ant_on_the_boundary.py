class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        distance = 0
        for i in range(len(nums)):
            distance += nums[i]
            if distance == 0:
                count += 1
        return count
