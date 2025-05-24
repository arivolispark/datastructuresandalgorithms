class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            if words[i].find(x) >= 0:
                result.append(i)
        return result
