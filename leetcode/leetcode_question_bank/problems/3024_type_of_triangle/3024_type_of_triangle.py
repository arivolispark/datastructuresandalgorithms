 def triangleType(self, nums: List[int]) -> str:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] = map.get(num) + 1
        
        if nums[0] + nums[1] <= nums[2] or nums[0] + nums[2] <= nums[1] or nums[1] + nums[2] <= nums[0]:
            return "none"
        else:
            if len(map) == 1:
                return "equilateral"
            elif len(map) == 2:
                return "isosceles"
            else:
                return "scalene"
