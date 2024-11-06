class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prevSetBits = 0
        prevMax, currMax, currMin = -math.inf, -math.inf, math.inf
        
        for num in nums:
            setBits = num.bit_count()
            if setBits != prevSetBits:
                if prevMax > currMin:
                    return False
                prevSetBits = setBits
                prevMax = currMax
                currMax = num
                currMin = num
            else:
                currMax = max(currMax, num)
                currMin = min(currMin, num)

        return prevMax <= currMin
