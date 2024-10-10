class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
      
        for index, value in enumerate(nums):
            if not stack or nums[stack[-1]] > value:
                stack.append(index)
              
        max_width = 0
      
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                max_width = max(max_width, i - stack.pop())
            if not stack:
                break
              
        return max_width
