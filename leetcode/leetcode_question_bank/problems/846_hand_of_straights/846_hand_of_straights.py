"""
Title:  846. Hand of Straights

Alice has some number of cards and she wants to rearrange the cards into groups
so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card
and an integer groupSize, return true if she can rearrange the cards, or false otherwise.



Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]


Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.


Constraints:
1) 1 <= hand.length <= 10^4
2) 0 <= hand[i] <= 10^9
3) 1 <= groupSize <= hand.length


Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

"""

from typing import List


class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        length = len(hand)
        map = {}

        if length % groupSize != 0:
            return False

        for i in range(length):
            map[hand[i]] = map.get(hand[i], 0) + 1

        while map:
            keys = list(map.keys())
            keys.sort()
            start = keys[0]

            for i in range(groupSize):
                if not map:
                    return False

                if start not in map:
                    return False

                map[start] -= 1
                if map[start] == 0:
                    del map[start]

                start += 1

        return True if not map else False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.isNStraightHand([1,2,3,6,2,3,4,7,8], 3), True)
    test(solution.isNStraightHand([1,2,3,4,5], 4), False)
    test(solution.isNStraightHand([8,10,12], 3), False)
