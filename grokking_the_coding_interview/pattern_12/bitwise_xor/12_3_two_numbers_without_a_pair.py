"""
PROBLEM STATEMENT:
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once.
Find the two numbers that appear only once.

Example 1:
Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]

Example 2:
Input: [2, 1, 3, 2]
Output: [1, 3]
"""


def find_two_numbers_without_a_pair(arr):
    num1_xor_num2 = 0

    n = len(arr)
    for i in range(n):
        num1_xor_num2 ^= arr[i]
    print("\n num1_xor_num2: ", num1_xor_num2, "\t bin(", num1_xor_num2, "): ", bin(num1_xor_num2))

    right_most_set_bit = 1
    while right_most_set_bit & num1_xor_num2 == 0:
        right_most_set_bit = right_most_set_bit << 1
    print("\n right_most_set_bit: ", right_most_set_bit, "\t bin(", right_most_set_bit, "): ", bin(right_most_set_bit))

    num1, num2 = 0, 0
    for i in range(n):
        if arr[i] & right_most_set_bit == 0:
            num1 ^= arr[i]
        else:
            num2 ^= arr[i]

    return [num1, num2]


if __name__ == "__main__":
    arr = 1, 4, 2, 1, 3, 5, 6, 2, 3, 5
    print("\n arr: ", arr)
    two_numbers_without_a_pair = find_two_numbers_without_a_pair(arr)
    print("\n two_numbers_without_a_pair: ", two_numbers_without_a_pair)
