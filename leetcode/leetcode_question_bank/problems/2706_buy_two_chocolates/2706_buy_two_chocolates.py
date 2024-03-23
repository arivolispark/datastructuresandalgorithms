from heapq import *

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_heap = []

        for i in range(len(prices)):
            heappush(min_heap, prices[i])

        if min_heap:
            p1 = heappop(min_heap)

        if min_heap:
            p2 = heappop(min_heap)

        if money - p1 - p2 >= 0:
            return money - p1 - p2
        else:
            return money
