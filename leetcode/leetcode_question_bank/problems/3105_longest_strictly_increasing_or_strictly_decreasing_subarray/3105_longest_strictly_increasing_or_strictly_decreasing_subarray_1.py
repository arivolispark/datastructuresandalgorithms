class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        increasing_length, decreasing_length = -math.inf, -math.inf
        increasing_list, decreasing_list = [], []
        
        for i in range(length):
            increasing_list.append(1)
            decreasing_list.append(1)

        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                increasing_list[i] = increasing_list[i - 1] + 1
        increasing_length = max(increasing_list)

        for i in range(1, length):
            if nums[i] < nums[i - 1]:
                decreasing_list[i] = decreasing_list[i - 1] + 1
        decreasing_length = max(decreasing_list)

        return max(increasing_length, decreasing_length)
