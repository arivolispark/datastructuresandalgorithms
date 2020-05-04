"""
Title:  Destination City

You are given the array paths, where paths[i] = [cityAi, cityBi] means
there exists a direct path going from cityAi to cityBi. Return the destination
city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop,
therefore, there will be exactly one destination city.



Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city
which is the destination city. Your trip consist of:
"London" -> "New York" -> "Lima" -> "Sao Paulo".


Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".


Example 3:
Input: paths = [["A","Z"]]
Output: "Z"


Constraints:

1) 1 <= paths.length <= 100
2) paths[i].length == 2
3) 1 <= cityAi.length, cityBi.length <= 10
4) cityAi != cityBi
5) All strings consist of lowercase and uppercase English letters and the space character.

"""

from typing import List


class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        if paths:
            destination_city_set = set()
            for i in range(len(paths)):
                source_destination_pair = paths[i]
                if source_destination_pair:
                    for j in range(len(source_destination_pair)):
                        destination_city_set.add(source_destination_pair[1])

            for i in range(len(paths)):
                source_destination_pair = paths[i]
                if source_destination_pair:
                    for j in range(len(source_destination_pair)):
                        if source_destination_pair[0] in destination_city_set:
                            destination_city_set.remove(source_destination_pair[0])
            return destination_city_set.pop()
        return ""


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]), "Sao Paulo")
    test(solution.destCity([["B", "C"], ["D", "B"], ["C", "A"]]), "A")
    test(solution.destCity([["A", "Z"]]), "Z")
