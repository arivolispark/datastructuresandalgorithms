class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        if s1 and s2:
            map1, map2 = {}, {}
            word_list_1 = s1.split(" ")
            word_list_2 = s2.split(" ")

            for i in range(len(word_list_1)):
                map1[word_list_1[i]] = map1.get(word_list_1[i], 0) + 1

            for i in range(len(word_list_2)):
                map2[word_list_2[i]] = map2.get(word_list_2[i], 0) + 1

            for k, v in map1.items():
                if v == 1:
                    if k not in map2:
                        result.append(k)

            for k, v in map2.items():
                if v == 1:
                    if k not in map1:
                        result.append(k)

        return result
