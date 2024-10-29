class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        result = -1
        s = set(nums)
        for v in nums:
            t = 0
            while v in s:
                v *= v
                t += 1
            if t > 1:
                result = max(result, t)
        return result
