class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_to_n_terms = n * (n + 1) // 2

        sum = 0
        for i in range(n):
            sum += nums[i]

        return sum_to_n_terms - sum
