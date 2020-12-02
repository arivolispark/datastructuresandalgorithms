"""
Title:  Shortest Word Distance

Given a list of words and two words word1 and word2, return the
shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3



Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""

from typing import List
import math

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        if words:
            if word1 and word2:
                distance = math.inf
                word1_index, word2_index = [], []

                for i in range(len(words)):
                    if words[i] == word1:
                        word1_index.append(i)
                    if words[i] == word2:
                        word2_index.append(i)

                for i in range(len(word1_index)):
                    for j in range(len(word2_index)):
                        distance = min(abs(word1_index[i] - word2_index[j]), distance)

                return distance


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"), 3)
    test(solution.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"), 1)
