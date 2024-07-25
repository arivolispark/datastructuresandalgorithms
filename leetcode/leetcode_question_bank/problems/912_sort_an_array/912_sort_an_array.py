from heapq import *

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_heap = []
        result = []
        
        for i in range(len(nums)):
            heappush(min_heap, nums[i])
        
        while min_heap:
            result.append(heappop(min_heap))
        
        return result
