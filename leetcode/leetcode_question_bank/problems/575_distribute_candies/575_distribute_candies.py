class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_dict = {}
        length = len(candyType)
        for i in range(length):
            if candyType[i] not in candy_dict:
                candy_dict[candyType[i]] = candyType[i]

        unique_candies = len(candy_dict)
        if unique_candies > length // 2:
            return length // 2
        elif unique_candies <= length // 2:
            return unique_candies
