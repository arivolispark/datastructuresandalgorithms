# Superstitious
# I am going to buy a house but I am little superstitious.
# I want the house number to add to an odd number. My scheme
# of adding is that I sum all the digits to obtain the total.
# If the total is less than 10 then I see if it is odd or not.
# If the sum is above 10, then I will add the digits again to
# get the new sum. I repeat this process till the sum is then
# 10. At that point I check if the sum is even or odd. If odd
# then I am good. Else I reject.

# Example:
# 101 -> 1 + 0 + 1 = 2 --> REJECT
# 149 -> 1 + 4 + 9 = 14 -> 1 + 4 = 5 --> ACCEPT

# Complete the function below to return True or False if the
# house numbers adds up to odd number.


def is_sum_odd(num):
    while num > 9:
        num = calculate_sum_of_digit(num)
    return num % 2 == 1


def calculate_sum_of_digit(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    nums = [(101, False),
            (149, True),
            (12345, False),
            (99999999999999999999999, True)]

    for num in nums:
        test(is_sum_odd(num[0]), num[1])