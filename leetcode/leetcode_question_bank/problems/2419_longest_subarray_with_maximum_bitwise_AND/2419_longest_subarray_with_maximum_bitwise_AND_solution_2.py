class Solution:
    def longestSubarray_1(self, nums: List[int]) -> int:
        max_val = max(nums)

        answer = 0
        streak = 0
        for i in range(len(nums)):
            if nums[i] == max_val:
                streak += 1
                answer = max(streak, answer)
            else:
                streak = 0
        return answer
