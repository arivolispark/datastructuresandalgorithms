class Solution:
    def finalString(self, s: str) -> str:
        result = []

        if s:
            for i in range(len(s)):
                if s[i] != 'i':
                    result.append(s[i])
                else:
                    result = result[::-1]

        return ''.join(result)        
