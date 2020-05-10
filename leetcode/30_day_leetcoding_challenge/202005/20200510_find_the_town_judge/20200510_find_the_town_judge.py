"""
Title:  Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a
rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing
that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the
town judge.  Otherwise, return -1.



Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2


Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3


Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1


Example 4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1


Example 5:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


Note:
1) 1 <= N <= 1000
2) trust.length <= 10000
3) trust[i] are all different
4) trust[i][0] != trust[i][1]
5) 1 <= trust[i][0], trust[i][1] <= N

"""

from typing import List


class Solution:

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judge = set()
        number_indegree_map = {}

        for i in range(1, N + 1):
            judge.add(i)
            number_indegree_map[i] = 0

        for i in range(len(trust)):
            trusting_person = trust[i][0]
            trusted_person = trust[i][1]

            if trusting_person in judge:
                judge.remove(trusting_person)
            number_indegree_map[trusted_person] += 1

        if len(judge) == 1:
            trusted_person = judge.pop()
            if number_indegree_map[trusted_person] == N - 1:
                return trusted_person
            else:
                return -1
        else:
            return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findJudge(2, [[1,2]]), 2)
    test(solution.findJudge(3, [[1,3],[2,3]]), 3)
    test(solution.findJudge(3, [[1,3],[2,3],[3,1]]), -1)
    test(solution.findJudge(3, [[1,2],[2,3]]), -1)
    test(solution.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]), 3)
    test(solution.findJudge(1, []), 1)
