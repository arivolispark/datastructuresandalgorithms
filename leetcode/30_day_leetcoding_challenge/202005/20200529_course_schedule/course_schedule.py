"""
Title:  Course Schedule

There are a total of numCourses courses you have
to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to
take course 0 you have to first take course 1, which
is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite
pairs, is it possible for you to finish all courses?



Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.


Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

1) The input prerequisites is a graph represented by a list of
edges, not adjacency matrices. Read more about how a graph is represented.
2) You may assume that there are no duplicate edges in the input prerequisites.
3) 1 <= numCourses <= 10^5

"""

from typing import List
import collections


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1 or len(prerequisites) == 0:
            return True

        indegree = collections.defaultdict(set)
        outdegree = collections.defaultdict(set)

        for course, prereq in prerequisites:
            outdegree[prereq].add(course)
            indegree[course].add(prereq)

        number_of_removed_connections = 0
        zero_indegree_node = []

        for i in range(numCourses):
            if not indegree[i]:
                zero_indegree_node.append(i)
                number_of_removed_connections += 1

        while zero_indegree_node:
            node = zero_indegree_node.pop()
            for i in outdegree[node]:
                indegree[i].remove(node)
                if not indegree[i]:
                    zero_indegree_node.append(i)
                    number_of_removed_connections += 1

        return number_of_removed_connections == numCourses


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.canFinish(1, [[]]), True)
    test(solution.canFinish(2, [[1,0]]), True)
    test(solution.canFinish(2, [[1,0],[0,1]]), False)
    test(solution.canFinish(3, [[0,1],[1,2],[2,1]]), False)
    test(solution.canFinish(3, [[1,0]]), True)
    test(solution.canFinish(3, [[1,0],[2,1]]), True)
    test(solution.canFinish(100, [[6,27],[83,9],[10,95],[48,67],[5,71],[18,72],[7,10],[92,4],[68,84],[6,41],[82,41],[18,54],[0,2],[1,2],[8,65],[47,85],[39,51],[13,78],[77,50],[70,56],[5,61],[26,56],[18,19],[35,49],[79,53],[40,22],[8,19],[60,56],[48,50],[20,70],[35,12],[99,85],[12,75],[2,36],[36,22],[21,15],[98,1],[34,94],[25,41],[65,17],[1,56],[43,96],[74,57],[19,62],[62,78],[50,86],[46,22],[10,13],[47,18],[20,66],[83,66],[51,47],[23,66],[87,42],[25,81],[60,81],[25,93],[35,89],[65,92],[87,39],[12,43],[75,73],[28,96],[47,55],[18,11],[29,58],[78,61],[62,75],[60,77],[13,46],[97,92],[4,64],[91,47],[58,66],[72,74],[28,17],[29,98],[53,66],[37,5],[38,12],[44,98],[24,31],[68,23],[86,52],[79,49],[32,25],[90,18],[16,57],[60,74],[81,73],[26,10],[54,26],[57,58],[46,47],[66,54],[52,25],[62,91],[6,72],[81,72],[50,35],[59,87],[21,3],[4,92],[70,12],[48,4],[9,23],[52,55],[43,59],[49,26],[25,90],[52,0],[55,8],[7,23],[97,41],[0,40],[69,47],[73,68],[10,6],[47,9],[64,24],[95,93],[79,66],[77,21],[80,69],[85,5],[24,48],[74,31],[80,76],[81,27],[71,94],[47,82],[3,24],[66,61],[52,13],[18,38],[1,35],[32,78],[7,58],[26,58],[64,47],[60,6],[62,5],[5,22],[60,54],[49,40],[11,56],[19,85],[65,58],[88,44],[86,58]]), False)
