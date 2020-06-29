"""
Title:  Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and
arrival airports [from, to], reconstruct the itinerary in order. All of
the tickets belong to a man who departs from JFK. Thus, the itinerary must
begin with JFK.


Note:
1) If there are multiple valid itineraries, you should return the itinerary
that has the smallest lexical order when read as a single string. For example,
the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
2) All airports are represented by three capital letters (IATA code).
3) You may assume all tickets form at least one valid itinerary.
4) One must use all the tickets once and only once.


Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]


Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.

"""

from typing import List


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.from_to_map = {}
        tickets.sort(key = lambda x: x[1])

        for key, value in tickets:
            if key in self.from_to_map:
                self.from_to_map[key].append(value)
            else:
                self.from_to_map[key] = [value]

        self.result = []
        self.dfs("JFK")

        return self.result[::-1]

    def dfs(self, airport):
        while airport in self.from_to_map and len(self.from_to_map[airport]) > 0:
            value = self.from_to_map[airport][0]
            self.from_to_map[airport].pop(0)
            self.dfs(value)
        self.result.append(airport)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]), ["JFK", "MUC", "LHR", "SFO", "SJC"])
    test(solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]), ["JFK","ATL","JFK","SFO","ATL","SFO"])
    test(solution.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]), ["JFK", "NRT", "JFK", "KUL"])
    test(solution.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
), ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"])
