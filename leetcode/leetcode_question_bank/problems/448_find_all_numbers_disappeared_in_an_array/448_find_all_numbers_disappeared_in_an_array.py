class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        map = {}
        
        for i in range(len(nums)):
            map[nums[i]] = nums[i]
        for i in range(1, len(nums) + 1):
            if i not in map:
                result.append(i)

        return result
