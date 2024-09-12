"""
Title:  1684. Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array of strings
words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.



Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.


Example 2:
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.


Example 3:
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.


Constraints:
1) 1 <= words.length <= 104
2) 1 <= allowed.length <= 26
3) 1 <= words[i].length <= 10
4) The characters in allowed are distinct.
5) words[i] and allowed contain only lowercase English letters.

"""

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        map = {}

        for i in range(len(allowed)):
            map[allowed[i]] = map.get(allowed[i], 0) + 1
        # print(" map: ", map)

        for i in range(len(words)):
            for j in range(len(words[i])):
                c = words[i][j]
                if c not in map:
                    break
            if c in map:
                count += 1
        return count


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]), 2)
    test(solution.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]), 7)
    test(solution.countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]), 4)
