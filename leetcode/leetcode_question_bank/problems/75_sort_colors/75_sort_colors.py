class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red = white = blue = 0
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        
        if 0 in map:
            red = map[0]
        if 1 in map:
            white = map[1]
        if 2 in map:
            blue = map[2]

        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif i < red + white:
                nums[i] = 1
            elif i < red + white + blue:
                nums[i] = 2
