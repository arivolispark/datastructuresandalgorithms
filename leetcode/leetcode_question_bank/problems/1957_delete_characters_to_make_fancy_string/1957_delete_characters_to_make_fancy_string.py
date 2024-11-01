"""
Title:  1957. Delete Characters to Make Fancy String

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.



Example 1:
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".


Example 2:
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".


Example 3:
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".


Constraints:
1) 1 <= s.length <= 10^5
2) s consists only of lowercase English letters.

"""


class Solution:

    def makeFancyString(self, s: str) -> str:
        result = []
        map = {}
        length = len(s)

        if length < 3:
            return s
        i = 2
        while i < length:
            first, second, third = s[i - 2], s[i - 1], s[i]
            if first == second == third:
                map[i] = i
            i += 1

        for i in range(length):
            if i not in map:
                result.append(s[i])
        return ''.join(result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.makeFancyString("leeetcode"), "leetcode")
    test(solution.makeFancyString("aaabaaaa"), "aabaa")
    test(solution.makeFancyString("aab"), "aab")
    test(solution.makeFancyString(""), "")
    test(solution.makeFancyString("a"), "a")
    test(solution.makeFancyString("aa"), "aa")
    test(solution.makeFancyString("aaa"), "aa")
    test(solution.makeFancyString("aab"), "aab")
