class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        map_1, map_2 = {}, {}

        for i in range(len(target)):
            map_1[target[i]] = map_1.get(target[i], 0) + 1
        for i in range(len(arr)):
            map_2[arr[i]] = map_2.get(arr[i], 0) + 1

        return True if map_1 == map_2 else False
