"""
Title:  Possible Bipartition

Given a set of N people (numbered 1, 2, ..., N), we would like
to split everyone into two groups of any size.

Each person may dislike some other people, and they should not
go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to
put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into
two groups in this way.


Example 1:
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]


Example 2:
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false


Example 3:
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:
1) 1 <= N <= 2000
2) 0 <= dislikes.length <= 10000
3) 1 <= dislikes[i][j] <= N
4) dislikes[i][0] < dislikes[i][1]
5) There does not exist i != j for which dislikes[i] == dislikes[j].

"""

from typing import List


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        person_map = {}
        visited = {}

        for persons in dislikes:
            if persons[0] not in person_map:
                person_map[persons[0]] = set([persons[1]])
            else:
                person_map[persons[0]].add(persons[1])

            if persons[1] not in person_map:
                person_map[persons[1]] = set([persons[0]])
            else:
                person_map[persons[1]].add(persons[0])

        for i in range(1, N + 1):
            if i not in visited:
                visited[i] = 0
                stack = [i]

                while stack:
                    person_1 = stack.pop()
                    if person_1 in person_map:
                        for person_2 in person_map[person_1]:
                            if person_2 in visited:
                                if visited[person_1] == visited[person_2]:
                                    return False
                            else:
                                visited[person_2] = (visited[person_1] + 1) % 2
                                stack.append(person_2)
        return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.possibleBipartition(4, [[1,2],[1,3],[2,4]]), True)
    test(solution.possibleBipartition(4, [[1,2],[1,3],[2,3]]), False)
    test(solution.possibleBipartition(4, [[1,2],[2,3],[3,4],[4,5],[1,5]]), False)
    test(solution.possibleBipartition(1, []), True)
    test(solution.possibleBipartition(10, [[4, 7], [4, 8], [2, 8], [8, 9], [1, 6], [5, 8], [1, 2], [6, 7], [3, 10], [8, 10], [1, 5], [7, 10], [1, 10], [3, 5], [3, 6], [1, 4], [3, 9], [2, 3], [1, 9], [7, 9], [2, 7], [6, 8], [5, 7], [3, 4]]), True)
    test(solution.possibleBipartition(5, [[1,2],[3,4],[4,5],[3,5]]), False)

    test(solution.possibleBipartition(50,
    [[9, 26], [1, 34], [14, 17], [29, 31], [10, 17], [25, 31], [22, 44], [36, 44], [26, 28], [17, 20], [16, 28],
     [18, 19], [11, 47], [34, 46], [17, 46], [15, 47], [19, 29], [44, 45], [14, 18], [1, 6], [28, 35], [16, 22],
     [10, 41], [13, 20], [2, 27], [18, 20], [8, 15], [37, 41], [2, 6], [24, 39], [13, 35], [10, 13], [18, 46], [8, 21],
     [1, 17], [2, 32], [14, 15], [5, 21], [27, 40], [8, 38], [5, 34], [29, 37], [20, 36], [9, 39], [31, 38], [8, 12],
     [7, 44], [14, 36], [4, 15], [17, 39], [2, 11], [25, 44], [15, 33], [20, 42], [25, 33], [19, 23], [48, 50],
     [28, 37], [1, 21], [23, 37], [40, 45], [10, 42], [2, 34], [13, 26], [11, 35], [1, 15], [42, 47], [24, 46], [4, 12],
     [8, 28], [15, 26], [14, 22], [21, 46], [4, 42], [8, 45], [12, 50], [16, 29], [2, 23], [16, 32], [11, 46], [5, 17],
     [15, 46], [20, 49], [43, 45], [17, 50], [7, 20], [2, 25], [21, 33], [8, 42], [16, 23], [29, 33], [11, 26],
     [29, 39], [32, 39], [13, 19], [27, 31], [8, 48], [12, 35], [3, 5], [16, 48], [4, 6], [19, 38], [8, 22], [14, 25],
     [5, 7], [10, 25], [26, 30], [23, 33], [22, 43], [1, 30], [7, 31], [16, 42], [5, 9], [1, 48], [4, 27], [44, 48],
     [15, 19], [21, 39], [49, 50], [30, 33], [12, 20], [7, 19], [31, 36], [36, 47], [34, 43], [42, 44], [24, 47],
     [31, 49], [38, 43], [8, 29], [15, 39], [4, 18], [19, 32], [14, 23], [20, 27], [30, 47], [4, 38], [28, 43], [1, 23],
     [23, 43], [6, 33], [4, 49], [11, 33], [2, 3], [18, 43], [14, 29], [12, 46], [3, 47], [6, 8], [15, 43], [27, 47],
     [22, 47], [12, 19], [28, 40], [35, 38], [1, 7], [8, 49], [7, 43], [14, 41], [30, 50], [17, 47], [20, 28], [13, 33],
     [19, 41], [18, 44], [8, 23], [13, 46], [20, 34], [29, 35], [15, 31], [20, 29], [2, 45], [7, 16], [23, 35],
     [30, 37], [12, 16], [5, 42], [16, 24], [3, 14], [17, 37], [6, 50], [25, 50], [15, 35], [5, 12], [12, 44], [10, 12],
     [5, 25], [19, 25], [24, 31], [39, 41], [31, 42], [1, 13], [9, 10], [8, 30], [24, 35], [3, 31], [3, 19], [20, 32],
     [27, 35], [6, 19], [1, 22], [32, 47], [5, 38], [10, 45], [3, 8], [42, 46], [35, 48], [26, 48]]), True)
