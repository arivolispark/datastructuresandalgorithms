"""
Title:  Task Scheduler

You are given a char array representing tasks CPU need to do. It contains capital
letters A to Z where each letter represents a different task. Tasks could be done
without the original order of the array. Each task is done in one unit of time. For
each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between
two same tasks (the same letter in the array), that is that there must be at least n units
of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish
all the given tasks.



Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.


Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.


Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A


Constraints:
1) The number of tasks is in the range [1, 10000].
2) The integer n is in the range [0, 100].

"""

from typing import List
from heapq import *


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        if tasks:
            task_frequency_map = {}
            max_heap = []

            for i in range(len(tasks)):
                task_frequency_map[tasks[i]] = task_frequency_map.get(tasks[i], 0) + 1

            for k, v in task_frequency_map.items():
                heappush(max_heap, (-v, k))
            #print(" max_heap: ", max_heap)

            while max_heap:
                wait_list = []
                k = n + 1
                while k > 0 and max_heap:
                    result += 1
                    frequency, task = heappop(max_heap)
                    if -frequency > 1:
                        wait_list.append((frequency + 1, task))
                    k -= 1

                for frequency, task in wait_list:
                    heappush(max_heap, (frequency, task))

                if max_heap:
                    result += k
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    #test(solution.leastInterval(["A","A","A","B","B","B"], 2), 8)
    #test(solution.leastInterval(["A","A","A","B","B","B"], 0), 6)
    test(solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2), 16)
