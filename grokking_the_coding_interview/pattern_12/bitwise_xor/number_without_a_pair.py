"""
PROBLEM STATEMENT:
In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:
Input: 1, 4, 2, 1, 3, 2, 3
Output: 4

Example 2:
Input: 7, 9, 7
Output: 9
"""


def find_number_without_a_pair(arr):
    n = len(arr)

    xor_value = 0
    for i in range(n):
        xor_value ^= arr[i]

    return xor_value


if __name__ == "__main__":
    arr = 1, 4, 2, 1, 3, 2, 3
    number_without_a_pair = find_number_without_a_pair(arr)
    print("\n number_without_a_pair: ", number_without_a_pair, "\t bin(number_without_a_pair): ", bin(number_without_a_pair))
