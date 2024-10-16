from heapq import *

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
      
        if a > 0:
            heappush(max_heap, [-a, 'a'])
        if b > 0:
            heappush(max_heap, [-b, 'b'])
        if c > 0:
            heappush(max_heap, [-c, 'c'])

        result = []
      
        while max_heap:
            current_char = heappop(max_heap)
          
            if len(result) >= 2 and result[-1] == current_char[1] and result[-2] == current_char[1]:
                if not max_heap:
                    break
                  
                next_char = heappop(max_heap)
              
                result.append(next_char[1])
                if -next_char[0] > 1:
                    next_char[0] += 1
                    heappush(max_heap, next_char)
              
                heappush(max_heap, current_char)
            else:
                result.append(current_char[1])

                if -current_char[0] > 1:
                    current_char[0] += 1
                    heappush(max_heap, current_char)

        return ''.join(result)
