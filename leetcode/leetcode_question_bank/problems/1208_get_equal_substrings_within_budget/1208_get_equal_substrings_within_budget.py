"""
Title:  1208. Get Equal Substrings Within Budget

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character
of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values
of the characters).

Return the maximum length of a substring of s that can be changed to be the same
as the corresponding substring of t with a cost less than or equal to maxCost. If there
is no substring from s that can be changed to its corresponding substring from t, return 0.



Example 1:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.


Example 2:
Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.


Example 3:
Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.


Constraints:
1) 1 <= s.length <= 10^5
2) t.length == s.length
3) 0 <= maxCost <= 10^6
4) s and t consist of only lowercase English letters.

"""


class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        result = 0
        left = 0
        current = 0

        for right in range(len(t)):
            current += abs(ord(s[right]) - ord(t[right]))

            while current > maxCost:
                current -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            result = max(result, right - left + 1)
        
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.equalSubstring("abcd", "bcdf", 3), 3)
    test(solution.equalSubstring("abcd", "cdef", 3), 1)
    test(solution.equalSubstring("abcd", "acde", 0), 1)
