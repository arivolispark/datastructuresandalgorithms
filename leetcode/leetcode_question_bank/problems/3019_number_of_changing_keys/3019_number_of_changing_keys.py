class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        last_key = s[0].upper()
        for i in range(1, len(s)):
            if s[i].upper() != last_key:
                count += 1
                last_key = s[i].upper()
        return count
