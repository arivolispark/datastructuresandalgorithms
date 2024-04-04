from heapq import *

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = 0
        apple_count = 0
        max_heap = []
        count = 0
        
        if apple:
            for i in range(len(apple)):
                total_apples += apple[i]
            
        if capacity:
            for i in range(len(capacity)):
                heappush(max_heap, -capacity[i])

            while max_heap:
                if apple_count < total_apples:
                    apple_count += -heappop(max_heap)
                    count += 1
                else: 
                    break
            
        return count
