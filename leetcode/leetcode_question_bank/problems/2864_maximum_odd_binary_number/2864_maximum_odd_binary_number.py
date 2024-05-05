class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            result.append(s[i])
        
        result.sort(reverse = True)

        for i in range(len(result)):
            if result[i] == "0":
                break
        result[i-1], result[len(result) - 1] = result[len(result) - 1], result[i-1]

        return ''.join(result)
