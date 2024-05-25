import collections

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counts = Counter(letters)

        @cache
        def get_score(index):
            f = Counter(words[index])
            score_val = 0
            for c, v in f.items():
                c = ord(c) - ord('a')
                score_val += score[c] * v
            return score_val

        def get_max(index, counts):
            if index == len(words):
                return 0

            result = 0
            result = max(result, get_max(index + 1, counts))

            f = collections.Counter(words[index])
            if counts >= f:
                counts -= f
                score = get_score(index)
                result = max(result, get_max(index + 1, counts) + score)
                counts += f

            return result
        return get_max(0, counts)
