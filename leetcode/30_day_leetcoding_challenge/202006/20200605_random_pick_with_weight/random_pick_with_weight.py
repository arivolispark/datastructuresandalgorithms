"""
Title:  Random Pick with Weight

Given an array w of positive integers, where w[i] describes the
weight of index i, write a function pickIndex which randomly
picks an index in proportion to its weight.

Note:

1) 1 <= w.length <= 10000
2) 1 <= w[i] <= 10^5
3) pickIndex will be called at most 10000 times.


Example 1:
Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]


Example 2:
Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]


Explanation of Input Syntax:

The input is two lists: the subroutines called and their
arguments. Solution's constructor has one argument, the
array w. pickIndex has no arguments. Arguments are always
wrapped with a list, even if there aren't any.

"""

from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.start = self.w[0]
        self.cumulative_w = []
        self.total_weight = 0
        self.weight_index_map = {}

        print("\n self.w: ", self.w)
        print(" self.start: ", self.start)
        print(" self.cumulative_w: ", self.cumulative_w)
        print(" self.total_weight: ", self.total_weight)
        print(" self.weight_index_map: ", self.weight_index_map)

        for i in range(len(w)):
            self.cumulative_w.append(self.total_weight + self.w[i])
            self.total_weight += self.w[i]

        print("\n self.w: ", self.w)
        print(" self.start: ", self.start)
        print(" self.cumulative_w: ", self.cumulative_w)
        print(" self.total_weight: ", self.total_weight)

    def pickIndex(self) -> int:
        import random

        random_value = random.random() * self.total_weight
        print("\n random_value: ", random_value)

        start, end = 0, len(self.cumulative_w) - 1
        while start < end:
            mid = start + (end - start) // 2
            if random_value > self.cumulative_w[mid]:
                start = mid + 1
            else:
                end = mid
        return start

    # Your Solution object will be instantiated and called as such:
    # obj = Solution(w)
    # param_1 = obj.pickIndex()


def find_index(nums: List[int], key: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == key:
            return mid
        elif nums[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    w = [1,3]
    #w = [1]

    print("\n w: ", w)

    solution = Solution(w)

    for i in range(5):
        random_pick = solution.pickIndex()
        print(" random_pick: ", random_pick)
