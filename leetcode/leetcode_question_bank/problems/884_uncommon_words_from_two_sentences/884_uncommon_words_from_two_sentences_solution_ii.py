class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        map_1, map_2 = {}, {}

        s1_str = s1.split(" ")
        for s in s1_str:
            map_1[s] = map_1.get(s, 0) + 1

        s2_str = s2.split(" ")
        for s in s2_str:
            map_2[s] = map_2.get(s, 0) + 1

        for k, v in map_1.items():
            if v == 1 and k not in map_2:
                result.append(k)
            
        for k, v in map_2.items():
            if v == 1 and k not in map_1:
                result.append(k)

        return result
