from heapq import * 

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_heap = []
        ranking_map = {}
        result = []

        if score:
            for s in score:
                heappush(max_heap, -s)
            
            ranking = 0
            while max_heap:
                value = -heappop(max_heap)
                ranking += 1
                
                if ranking == 1:
                    ranking_map[value] = "Gold Medal"
                elif ranking == 2:
                    ranking_map[value] = "Silver Medal"
                elif ranking == 3:
                    ranking_map[value] = "Bronze Medal"
                else:
                    ranking_map[value] = str(ranking)

            for num in score:
                result.append(ranking_map[num])

        return result
