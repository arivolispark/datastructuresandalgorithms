"""
Title:  28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in
haystack, or -1 if needle is not part of haystack.


Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.


Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:
1) 1 <= haystack.length, needle.length <= 104
2) haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is not None and needle is not None:
            haystack_length, needle_length = len(haystack), len(needle)

            if haystack_length < needle_length:
                return -1
            if haystack_length == 0 and needle_length == 0:
                return 0
            if haystack == needle:
                return 0

            h_start, h_end = 0, haystack_length - 1
            n_start, n_end = 0, needle_length - 1
            match_count = 0

            while h_start <= h_end - needle_length + 1:
                if haystack[h_start] == needle[n_start]:
                    i, j = 0, 0

                    while j <= n_end:
                        if haystack[h_start + j] == needle[n_start + j]:
                            match_count += 1
                        else:
                            match_count = 0
                            break

                        j += 1

                    if match_count == needle_length:
                        return h_start

                h_start += 1
            return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.strStr("", ""), 0)
    test(solution.strStr("sadbutsad", "sad"), 0)
    test(solution.strStr("leetcode", "leeto"), -1)
    test(solution.strStr("hello", "ll"), 2)
    test(solution.strStr("a", "a"), 0)
    test(solution.strStr("aaa", "aaaa"), -1)
    test(solution.strStr("mississippi", "issip"), 4)
    test(solution.strStr("abc", "c"), 2)
    test(solution.strStr("mississippi", "a"), -1)
    test(solution.strStr("mississippi", "pi"), 9)
