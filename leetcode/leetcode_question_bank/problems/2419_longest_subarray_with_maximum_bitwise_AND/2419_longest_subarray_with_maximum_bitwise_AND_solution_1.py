class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = nums[0]
        curr_len = 1
        max_len = 1

        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                curr_len = 1
                max_len = 1
            elif nums[i] == max_val:
                curr_len += 1
                max_len = max(curr_len, max_len)
            else:
                curr_len = 0

        return max_len
