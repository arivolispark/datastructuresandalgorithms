class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absent_count += 1
                if absent_count == 2:
                    return False
            elif s[i] == 'L':
                if (i - 1) >= 0 and (i - 2) >= 0 and s[i - 1] == 'L' and s[i - 2] == 'L':
                    return False
                    
        return True
