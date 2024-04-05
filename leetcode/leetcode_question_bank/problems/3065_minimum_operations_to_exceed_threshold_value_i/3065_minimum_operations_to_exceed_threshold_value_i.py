from heapq import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations_count = 0
        if nums:
            min_heap = []
            for i in range(len(nums)):
                heappush(min_heap, nums[i])

            while min_heap:
                x = heappop(min_heap)
                if x >= k:
                    break
                else:
                    operations_count += 1
        return operations_count
