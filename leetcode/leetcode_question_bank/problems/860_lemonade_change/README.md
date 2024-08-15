"""
Title:  860. Lemonade Change

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to
buy from you and order one at a time (in the order specified by bills). Each customer
will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide
the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return
true if you can provide every customer with the correct change, or false otherwise.



Example 1:
Input: bills = [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.


Example 2:
Input: bills = [5,5,10,10,20]
Output: false
Explanation:
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.


Constraints:
1) 1 <= bills.length <= 10^5
2) bills[i] is either 5, 10, or 20.

"""

from typing import List


class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        map = {}

        for i in range(len(bills)):
            map[bills[i]] = map.get(bills[i], 0) + 1

            if bills[i] == 10:
                if 5 in map and map[5] > 0:
                    map[5] -= 1
                else:
                    return False
            elif bills[i] == 20:
                if 10 in map and map[10] > 0 and 5 in map and map[5] > 0:
                    map[10] -= 1
                    map[5] -= 1
                elif 10 in map and map[10] > 0 and 5 in map and map[5] == 0:
                    return False
                elif 10 in map and map[10] == 0 and 5 in map and map[5] >= 3:
                    map[5] -= 3
                elif 10 in map and map[10] == 0 and 5 in map and map[5] < 3:
                    return False
                elif 10 not in map and 5 in map and map[5] >= 3:
                    map[5] -= 3
                elif 10 not in map and 5 in map and map[5] < 3:
                    return False

        return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.lemonadeChange([5,5,5,10,20]), True)
    test(solution.lemonadeChange([5,5,10,10,20]), False)
    test(solution.lemonadeChange([5,5,5,5,20,20,5,5,20,5]), False)
    test(solution.lemonadeChange([5,5,5,20,20,10,5,10,10,20]), False)
