class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        map = {}

        if s:
            i, j = 0, len(s) - 1
            while i < j:
                a = s[i] + s[i + 1]
                map[a] = map.get(a, 0) + 1
                i += 1

            reverse_s = s[::-1]
            i, j = 0, len(reverse_s) - 1
            while i < j:
                a = reverse_s[i] + reverse_s[i + 1]
                if a in map:
                    return True
                i += 1

            return False
