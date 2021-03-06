"""
Title:  Power of Two


Given a string s and a string t, check if s
is subsequence of t.

A subsequence of a string is a new string which
is formed from the original string by deleting
some (can be none) of the characters without disturbing
the relative positions of the remaining characters.
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk
where k >= 1B, and you want to check one by one to see
if T has its subsequence. In this scenario, how would you
change your code?


Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.


Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true


Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:
1) 0 <= s.length <= 100
2) 0 <= t.length <= 10^4
3) Both strings consists only of lowercase characters.

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s and t:
            s_len, t_len = len(s), len(t)

            if s_len == t_len == 0:
                return True

            i, j = 0, 0

            while i < s_len and j < t_len:
                if s[i] == t[j]:
                    i += 1
                j += 1

            return i == s_len


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.isSubsequence(None, "ahbgdc"), None)
    test(solution.isSubsequence("abc", None), None)
    test(solution.isSubsequence(None, None), None)
    test(solution.isSubsequence("abc", "ahbgdc"), True)
    test(solution.isSubsequence("axc", "ahbgdc"), False)
