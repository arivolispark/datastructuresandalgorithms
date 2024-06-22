"""
Title:  1052. Grumpy Bookstore Owner

There is a bookstore owner that has a store open for n minutes. Every
minute, some number of customers enter the store. You are given an integer
array customers of length n where customers[i] is the number of the customer
that enters the store at the start of the ith minute and all those customers
leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array
grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith
minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not
satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy
for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.



Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.


Example 2:
Input: customers = [1], grumpy = [0], minutes = 1
Output: 1


Constraints:
1) n == customers.length == grumpy.length
2) 1 <= minutes <= n <= 2 * 104
3) 0 <= customers[i] <= 1000
4) grumpy[i] is either 0 or 1.

"""

from typing import List


class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        length = len(customers)
        satisfied_sum = 0

        for i in range(length):
            if grumpy[i] == 0:
                satisfied_sum += customers[i]

        left = 0
        window_sum, max_window_sum = 0, 0

        for right in range(length):
            if grumpy[right]:
                window_sum += customers[right]

            if right - left + 1 > minutes:
                if grumpy[left]:
                    window_sum -= customers[left]
                left += 1
            max_window_sum = max(window_sum, max_window_sum)
        return satisfied_sum + max_window_sum


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1], 3), 16)
    test(solution.maxSatisfied([1],[0], 1), 1)
