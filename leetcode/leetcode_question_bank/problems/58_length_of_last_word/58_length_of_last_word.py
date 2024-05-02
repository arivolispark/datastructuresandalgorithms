class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s:
            words = s.split(" ")
            words = words[::-1]
            for i in range(len(words)):
                if len(words[i]) > 0:
                    return len(words[i])  
