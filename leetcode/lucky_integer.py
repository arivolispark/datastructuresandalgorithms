"""
Title:  Lucky integer

Find Lucky Integer in an Array.  Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer
return -1.


Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.


Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.


Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.


Time: O(N)
Space:  O(N)
"""


def lucky_int(arr):
    """
    Time: O(N)
    Space:  O(N)
    """
    number_frequency_map = {}

    for num in arr:  # O(N)
        number_frequency_map[num] = number_frequency_map.get(num, 0) + 1

    lucky_number = -1
    for key, value in number_frequency_map.items():  # O(N)
        if key == value:
            lucky_number = max(value, lucky_number)

    return lucky_number


def lucky_int_2(arr):
    """
    Time: O(N^2)
    Space:  O(N)
    """

    lucky_list = []
    for i in arr:  # O(N)
        if arr.count(i) == i:  # O(N)
            lucky_list.append(i)
    if lucky_list:
        return max(lucky_list)
    else:
        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    test(lucky_int([2, 2, 3, 4]), 2)
    test(lucky_int([1, 2, 2, 3, 3, 3]), 3)
    test(lucky_int([2, 2, 2, 3, 3]), -1)
    test(lucky_int([5]), -1)
    test(lucky_int([7, 7, 7, 7, 7, 7, 7]), 7)
