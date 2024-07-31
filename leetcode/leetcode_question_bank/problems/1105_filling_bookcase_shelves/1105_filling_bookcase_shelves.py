class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0] + [math.inf] * len(books)

        for i in range(len(books)):
            sum_thickness = 0
            max_height = 0
            for j in range(i, -1, -1):
                thickness, height = books[j]
                sum_thickness += thickness
                if sum_thickness > shelfWidth:
                    break
                max_height = max(max_height, height)
                dp[i + 1] = min(dp[i + 1], dp[j] + max_height)

        return dp[-1]
