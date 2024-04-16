class Solution:
    def findLatestTime(self, s: str) -> str:
        result = []

        for i in range(len(s)):
            result.append(s[i])

        if result[0] == '?' and result[1] == '?':
            result[0] = '1'
            result[1] = '1'
        elif result[0] == '?':
            if result[1] == '0':
                result[0] = '1'
                result[1] = '0'
            elif result[1] == '1':
                result[0] = '1'
                result[1] = '1'
            else:
                result[0] = '0'
        elif result[0] == '0' and result[1] == '?':
            result[0] = '0'
            result[1] = '9'
        elif result[0] == '1' and result[1] == '?':
            result[0] = '1'
            result[1] = '1'

        if result[3] == '?':
            result[3] = '5'
        if result[4] == '?':
            result[4] = '9'

        return ''.join(result)
