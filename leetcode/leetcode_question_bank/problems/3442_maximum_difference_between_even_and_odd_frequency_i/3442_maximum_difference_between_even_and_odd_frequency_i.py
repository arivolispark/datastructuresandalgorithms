class Solution:
    def maxDifference(self, s: str) -> int:
        map = {}
        max_odd_v, max_even_v, min_odd_v, min_even_v = -math.inf, -math.inf, math.inf, math.inf
        diff1, diff2 = 0, 0
        
        for i in range(len(s)):
            map[s[i]] = map.get(s[i], 0) + 1
        
        for k, v in map.items():
            if v % 2 == 0:
                max_even_v = max(max_even_v, v)
                min_even_v = min(min_even_v, v)
            else:
                max_odd_v = max(max_odd_v, v)
                min_odd_v = min(min_odd_v, v)

        diff1 = max_odd_v - min_even_v
        diff2 = min_odd_v - max_even_v

        return max(diff1, diff2)
