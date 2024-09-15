class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        answer = 0
        kVowels = 'aeiou'
        prefix = 0  # the binary prefix
        prefixToIndex = {0: -1}

        for i, c in enumerate(s):
            index = kVowels.find(c)
            if index != -1:
                prefix ^= 1 << index
            prefixToIndex.setdefault(prefix, i)
            answer = max(answer, i - prefixToIndex[prefix])

        return answer
