import math

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum, digit_sum = 0, 0

        if nums:
            for i in range(len(nums)):
                element_sum += nums[i]
                digit_sum += get_digit_sum(nums[i])
        return abs(element_sum - digit_sum)


def get_digit_sum(num: int) -> int:
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum
