"""
Title:  Find All Anagrams in a String

Given a string s and a non-empty string p, find all the
start indices of p's anagrams in s.

Strings consists of lowercase English letters only and
the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.


Example 1:
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Example 2:
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

from typing import List
from collections import Counter


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if s and p:
            s_length, p_length = len(s), len(p)
            if s_length < p_length:
                return []

            p_char_frequency = Counter(p)
            s_char_frequency = Counter()

            result = []
            for i in range(s_length):
                s_char_frequency[s[i]] += 1
                if i >= p_length:
                    if s_char_frequency[s[i - p_length]] == 1:
                        del s_char_frequency[s[i - p_length]]
                    else:
                        s_char_frequency[s[i - p_length]] -= 1
                if p_char_frequency == s_char_frequency:
                    result.append(i - p_length + 1)
            return result
        return None


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findAnagrams(None, None), None)
    test(solution.findAnagrams(None, ""), None)
    test(solution.findAnagrams(None, "a"), None)
    test(solution.findAnagrams(None, "ab"), None)
    test(solution.findAnagrams("", ""), None)
    test(solution.findAnagrams("", "a"), None)
    test(solution.findAnagrams("", "ab"), None)
    test(solution.findAnagrams("cbaebabacd", "abc"), [0, 6])
    test(solution.findAnagrams("abab", "ab"), [0, 1, 2])
    test(solution.findAnagrams("abacbabc", "abc"), [1, 2, 3, 5])
