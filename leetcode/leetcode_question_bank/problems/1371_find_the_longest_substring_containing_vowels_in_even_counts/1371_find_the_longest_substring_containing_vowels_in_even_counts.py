class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        answer = 0
        vowels = "aeiou"
        prefix = 0  # the binary prefix
        prefix_to_index = {0: -1}

        for i, c in enumerate(s):
            index = vowels.find(c)
            if index != -1:
                prefix ^= 1 << index
            prefix_to_index.setdefault(prefix, i)
            answer = max(answer, i - prefix_to_index[prefix])

        return answer
