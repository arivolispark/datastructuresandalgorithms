class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result, temp = [], []
        for i in range(len(s)):
            if ord(s[i]) != 45:
                temp.append(s[i].upper())

        temp = temp[::-1]

        count = 0
        i = 0
        while i < len(temp):
            if count < k:
                result.append(temp[i])
                count += 1
            elif count == k:
                result.append("-")
                count = 0
                i -= 1
            i += 1

        result = result[::-1]
        return ''.join(result)
