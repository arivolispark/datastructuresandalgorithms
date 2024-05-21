import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])
        for i in range(len(nums)):
            result += itertools.combinations(nums, i + 1)
        result = [ list(t) for t in result ]
        return result
