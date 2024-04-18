class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        map = {}

        if words:
            for i in range(len(words)):
                w = words[i][::-1]
                if w not in map:
                    map[words[i]] = w
                else:
                    count += 1
        return count
