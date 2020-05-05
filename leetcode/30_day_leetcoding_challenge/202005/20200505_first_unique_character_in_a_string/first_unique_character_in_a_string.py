"""
Title:  First Unique Character in a String

Given a string, find the first non-repeating character in
it and return it's index. If it doesn't exist, return -1.


Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.


Note: You may assume the string contain only lowercase letters.

"""


class Solution:

    def firstUniqChar(self, s: str) -> int:
        if s:
            character_freq_map = {}
            for i in range(len(s)):
                character_freq_map[s[i]] = character_freq_map.get(s[i], 0) + 1
            for i in range(len(s)):
                if character_freq_map[s[i]] == 1:
                    return i
        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.firstUniqChar("leetcode"), 0)
    test(solution.firstUniqChar("loveleetcode"), 2)

