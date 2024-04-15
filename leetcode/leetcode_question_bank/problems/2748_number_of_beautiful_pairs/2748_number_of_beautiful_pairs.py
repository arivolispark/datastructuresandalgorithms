class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        map = {}
        count = 0

        if nums:
            for i in range(len(nums)):
                digits = get_digits(nums[i])
                map[nums[i]] = digits

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    i_digits = map.get(nums[i])
                    j_digits = map.get(nums[j])

                    i_first_digit = i_digits[0]
                    j_last_digit = j_digits[-1]

                    largest_divisor = gcd(i_first_digit, j_last_digit)

                    if is_coprime(largest_divisor):
                        count += 1
        return count


def is_coprime(num: int) -> bool:
    return True if num == 1 else False


def gcd(digit1: int, digit2: int) -> int:
    factors1, factors2 = {}, {}
    largest_divisor = 1

    for i in range(1, digit1 + 1):
        if digit1 % i == 0:
            factors1[i] = i

    for i in range(1, digit2 + 1):
        if digit2 % i == 0:
            factors2[i] = i

    for k in factors1.keys():
        if k in factors2:
            largest_divisor = max(k, largest_divisor)

    return largest_divisor


def get_digits(num: int) -> List[int]:
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits = digits[::-1]
    return digits
