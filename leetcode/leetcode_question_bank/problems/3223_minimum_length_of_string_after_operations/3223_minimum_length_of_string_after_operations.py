from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        result = 0
        counter = Counter(s)
        
        for k, v in counter.items():
            if v & 1:
                result += 1
            else:
                result += 2

        return result
