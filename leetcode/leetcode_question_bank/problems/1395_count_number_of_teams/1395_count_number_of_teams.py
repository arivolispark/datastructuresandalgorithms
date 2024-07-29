class Solution:
    def numTeams(self, rating: List[int]) -> int:
        length = len(rating)
        result = 0
        
        for i in range(length):
            less_before, greater_before = 0, 0
            less_after, greater_after = 0, 0
            
            for j in range(i):
                if rating[j] < rating[i]:
                    less_before += 1
                elif rating[j] > rating[i]:
                    greater_before += 1
            
            for j in range(i + 1, length):
                if rating[j] < rating[i]:
                    less_after += 1
                elif rating[j] > rating[i]:
                    greater_after += 1
            
            result += less_before * greater_after + greater_before * less_after
        return result
