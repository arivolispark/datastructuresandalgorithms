from heapq import *

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(min_heap)

        max_range = max(row[0] for row in nums)
        min_range = heapq.nsmallest(1, min_heap)[0][0]
        result = [min_range, max_range]

        while len(min_heap) == len(nums):
            num, r, c = heapq.heappop(min_heap)
            if c + 1 < len(nums[r]):
                heapq.heappush(min_heap, (nums[r][c + 1], r, c + 1))
                max_range = max(max_range, nums[r][c + 1])
                min_range = heapq.nsmallest(1, min_heap)[0][0]
                if max_range - min_range < result[1] - result[0]:
                    result[0], result[1] = min_range, max_range

        return result
