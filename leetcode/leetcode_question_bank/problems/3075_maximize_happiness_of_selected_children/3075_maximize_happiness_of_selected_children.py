import math

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        result = 0
        reduction_factor = 0
        
        happiness.sort(reverse = True)

        for i in range(k):
            result += max(0, happiness[i] - reduction_factor)
            reduction_factor += 1

        return result
