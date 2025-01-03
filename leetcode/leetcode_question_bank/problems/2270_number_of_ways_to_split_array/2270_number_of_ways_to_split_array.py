class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0
        total = sum(nums)

        progressive_sum_list = []
        progressive_sum = nums[0]

        progressive_sum_list.append(progressive_sum)        

        for i in range(1, len(nums) - 1):
            progressive_sum += nums[i]
            progressive_sum_list.append(progressive_sum)

        for i in range(len(progressive_sum_list)):
            if progressive_sum_list[i] >= total - progressive_sum_list[i]:
                result += 1
             
        return result
