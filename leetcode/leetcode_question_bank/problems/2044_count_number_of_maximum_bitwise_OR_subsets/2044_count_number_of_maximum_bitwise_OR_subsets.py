class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = result = 0
        for x in nums:
            mx |= x

        def dfs(i, t):
            nonlocal mx, result
            if i == len(nums):
                if t == mx:
                    result += 1
                return
            dfs(i + 1, t)
            dfs(i + 1, t | nums[i])

        dfs(0, 0)
        return result
