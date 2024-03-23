import math
from heapq import *

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest_value = -math.inf
        largest_value_index = -1
        max_heap = []

        for i in range(len(nums)):
            val = nums[i]
            if val > largest_value:
                largest_value = val
                largest_value_index = i
            heappush(max_heap, -val)

        if max_heap:
            l1 = -heappop(max_heap)

        if max_heap:
            l2 = -heappop(max_heap)

        if l1 // 2 >= l2:
            return largest_value_index
        else:
            return -1
