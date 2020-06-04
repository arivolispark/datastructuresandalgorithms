"""
Title:  Last Stone Weight

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones
have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this
stone (or 0 if there are no stones left.)



Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


Note:
1) 1 <= stones.length <= 30
2) 1 <= stones[i] <= 1000

"""

from typing import List
from heapq import *


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        if stones:
            for stone in stones:
                heappush(max_heap, -stone)

            while len(max_heap) > 0:
                if len(max_heap) == 1:
                    return -heappop(max_heap)
                else:
                    first_heaviest_stone = -heappop(max_heap)
                    second_heaviest_stone = -heappop(max_heap)
                    diff = first_heaviest_stone - second_heaviest_stone
                    if diff > 0:
                        heappush(max_heap, -diff)
            return 0
        return 0


def get_test_case_1() -> List[int]:
    return None


def get_test_case_2() -> List[int]:
    return []


def get_test_case_3() -> List[int]:
    return [12]


def get_test_case_4() -> List[int]:
    return [12, 17]


def get_test_case_5() -> List[int]:
    return [2, 2]


def get_test_case_6() -> List[int]:
    return [2, 3]


def get_test_case_7() -> List[int]:
    return [2, 7, 4, 2, 7, 4]


def get_test_case_8() -> List[int]:
    return [2, 7, 4, 1, 8, 1]


if __name__ == "__main__":
    solution = Solution()

    #stones = get_test_case_1()
    #stones = get_test_case_2()
    #stones = get_test_case_3()
    #stones = get_test_case_4()
    #stones = get_test_case_5()
    #stones = get_test_case_6()
    #stones = get_test_case_7()
    stones = get_test_case_8()
    print("\n stones: ", stones)

    last_stone_weight =  solution.lastStoneWeight(stones)
    print("\n last_stone_weight: ", last_stone_weight)
