class Solution:
    def minimumPushes(self, word: str) -> int:
        result = 0

        # Time:  𝑂(𝑛)
        # Space:  O(26) = O(1)
        
        frequency = sorted(collections.Counter(word).values(), reverse = True)
        for i, freq in enumerate(frequency):
            result += freq * (i // 8 + 1)  
        return result
