import math

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_num = -math.inf
        map = {}

        if nums:
            for i in range(len(nums)):
                max_num = max(nums[i], max_num)
                map[nums[i]] = map.get(nums[i], 0) + 1

            if len(nums) != max_num + 1:
                return False

            if map[max_num] != 2:
                return False

            for i in range(1, max_num - 1, 1):
                if i not in map:
                    return False
                elif map[i] != 1:
                    return False

        return True
