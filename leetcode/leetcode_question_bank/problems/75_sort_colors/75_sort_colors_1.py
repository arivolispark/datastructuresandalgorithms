class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1

        r, w, b = 0, 0, 0

        if 0 in map:
            r = map[0]
        if 1 in map:
            w = map[1]
        if 2 in map:
            b = map[2]

        for i in range(r):
            nums[i] = 0
        for i in range(r, r + w):
            nums[i] = 1
        for i in range(r + w, r + w + b):
            nums[i] = 2
