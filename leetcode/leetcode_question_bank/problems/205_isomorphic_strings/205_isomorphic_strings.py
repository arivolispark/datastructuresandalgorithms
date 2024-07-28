class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        s_len, t_len = len(s), len(t)
        
        if s_len != t_len:
            return False

        for i in range(s_len):
            if s[i] in map:
                v = map[s[i]]
                if t[i] != v:
                    return False
            else:
                if t[i] in map.values():
                    return False
                map[s[i]] = t[i]

        return True
