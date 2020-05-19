"""
Title:  Permutation in String

Given two strings s1 and s2, write a function to return true
if s2 contains the permutation of s1. In other words, one of
the first string's permutations is the substring of the second string.


Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").


Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False


Note:
    1) The input strings only contain lower case letters.
    2) The length of both given strings is in range [1, 10,000].

"""

from typing import List
from collections import Counter


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 and s2:
            s1_length, s2_length = len(s1), len(s2)
            if s1_length > s2_length:
                return False

            s1_char_frequency = Counter(s1)
            s2_char_frequency = Counter()

            for i in range(s2_length):
                s2_char_frequency[s2[i]] += 1
                if i >= s1_length:
                    if s2_char_frequency[s2[i - s1_length]] == 1:
                        del s2_char_frequency[s2[i - s1_length]]
                    else:
                        s2_char_frequency[s2[i - s1_length]] -= 1

                if s1_char_frequency == s2_char_frequency:
                    return True
            return False
        return False

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

    test(solution.checkInclusion("ab", "eidbaooo"), True)
    test(solution.checkInclusion("ab", "eidboaoo"), False)
    test(solution.checkInclusion("a", "ab"), True)
