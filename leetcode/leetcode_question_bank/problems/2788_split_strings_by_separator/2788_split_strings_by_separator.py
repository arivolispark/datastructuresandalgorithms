class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        if words:
            for i in range(len(words)):
                words_list = words[i].split(separator)
                if words_list:
                    for j in range(len(words_list)):
                        if len(words_list[j]) > 0:
                            result.append(words_list[j])
        return result
