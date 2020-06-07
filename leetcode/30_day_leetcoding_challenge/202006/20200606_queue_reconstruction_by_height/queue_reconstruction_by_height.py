"""
Title:  Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each
person is described by a pair of integers (h, k), where h is the height
of the person and k is the number of people in front of this person who
have a height greater than or equal to h. Write an algorithm to reconstruct
the queue.


Note:
The number of people is less than 1,100.


Example:
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""

from typing import List


class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if people:
            result = []
            people = sorted(people, key = lambda x: (-x[0], x[1]))

            for p in people:
                result.insert(p[1], p)
            return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.reconstructQueue(None), None)
    test(solution.reconstructQueue([]), None)
    test(solution.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]), [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]])

