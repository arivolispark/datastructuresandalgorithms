class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if words:
            l = []
            for i in range(len(words)):
                l.append(words[i][0])

            acronym = ''.join(l)

            return True if acronym == s else False
