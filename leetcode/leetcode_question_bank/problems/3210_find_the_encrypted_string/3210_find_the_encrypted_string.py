class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        result = []
        length = len(s)
        for i in range(length):
            result.append(s[(i + k) % length])
        return ''.join(result)
