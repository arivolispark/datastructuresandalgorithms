class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if get_digits(nums[i]) == True:
                result += 1
        return result

def get_digits(num: int) -> bool:
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10

    return True if len(digits) % 2 == 0 else False
