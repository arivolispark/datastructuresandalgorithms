"""
Title:  140.  Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct
a sentence where each word is a valid dictionary word. Return all such possible sentences
in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]


Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.


Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []


Constraints:
1) 1 <= s.length <= 20
2) 1 <= wordDict.length <= 1000
3) 1 <= wordDict[i].length <= 10
4) s and wordDict[i] consist of only lowercase English letters.
5) All the strings of wordDict are unique.
6) Input is generated in a way that the length of the answer doesn't exceed 10^5.

"""

from typing import List

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = set(wordDict)

        result = []

        def construct(index, current):
            if index == len(s):
                result.append(" ".join(current))
                return

            for end in range(index, len(s)):
                if s[index:end + 1] in d:
                    current.append(s[index:end + 1])
                    construct(end + 1, current)
                    current.pop()

        construct(0, [])
        return result


def get_test_case_1_output(result: List[str]) -> bool:
    expected = set()
    expected.add('cat sand dog')
    expected.add('cats and dog')

    if len(result) > 0:
        for c in result:
            assert c in expected
    return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    result = solution.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
    assert get_test_case_1_output(result)

    result = solution.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])
    assert get_test_case_1_output(result)

    # #test(solution.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]), ["pine apple pen apple","pineapple pen apple","pine applepen apple"])
    # #test(solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]), [])
