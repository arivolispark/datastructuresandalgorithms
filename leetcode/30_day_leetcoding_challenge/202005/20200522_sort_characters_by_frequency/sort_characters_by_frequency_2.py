"""
Title:  Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.


Example 1:
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


Example 2:
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.


Example 3:
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""

from collections import Counter
from heapq import *


class Solution:

    def frequencySort(self, s: str) -> str:
        result = ""
        char_frequency = Counter(s)
        max_heap = []

        for char, frequency in char_frequency.items():
            heappush(max_heap, (-frequency, char))

        while max_heap:
            frequency, char = heappop(max_heap)
            result += -frequency * char

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.frequencySort(None), "")
    test(solution.frequencySort(""), "")
    test(solution.frequencySort("b"), "b")
    test((solution.frequencySort("tree")), "eetr")
    test((solution.frequencySort("tree")), "eert")
    test((solution.frequencySort("cccaaa")), "cccaaa")
    test((solution.frequencySort("cccaaa")), "aaaccc")
    test(solution.frequencySort("Aabb"), "bbAa")
    test(solution.frequencySort("Aabb"), "bbaA")
