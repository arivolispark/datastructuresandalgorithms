class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        @functools.lru_cache(None)
        def dp(i: int, j: int):
            if i == len(target):
                return 1
            if j == wordLength:
                return 0
            return (dp(i + 1, j + 1) * counts[j][target[i]] + dp(i, j + 1)) % kMod


        kMod = 1_000_000_007
        wordLength = len(words[0])
        counts = [collections.Counter() for _ in range(wordLength)]

        for i in range(wordLength):
            for word in words:
                counts[i][word[i]] += 1

        return dp(0, 0)
