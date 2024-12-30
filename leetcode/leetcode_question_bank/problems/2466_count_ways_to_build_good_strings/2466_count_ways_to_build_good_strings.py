class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        result = 0
        kMod = 1_000_000_007
        dp = [1] + [0] * high

        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % kMod
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % kMod
            if i >= low:
                result = (result + dp[i]) % kMod

        return result
