class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            while high >= low and nums[high] == val:
                high -= 1
            while low <= high and nums[low] != val:
                low += 1

            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
        return high + 1
