class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp, result = [], []
        map = {}
        length = len(arr)

        for i in range(length):
            temp.append(arr[i])

        temp.sort()

        rank = 1
        for i in range(length):
            if temp[i] not in map:
                map[temp[i]] = rank
                rank += 1

        for i in range(length):
            result.append(map[arr[i]])

        return result
