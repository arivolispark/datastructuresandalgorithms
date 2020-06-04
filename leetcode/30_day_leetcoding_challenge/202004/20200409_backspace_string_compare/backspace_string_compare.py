"""
Title:    Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.


Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 2:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1) 1 <= S.length <= 200
2) 1 <= T.length <= 200
3) S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?



Time:  O(N)
Space:  O(1)
"""


from collections import deque


class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        return get_editted_string(S) == get_editted_string(T)


def get_editted_string(S: str) -> str:
    q = deque()

    for chr in S:
        if chr != "#":
            q.append(chr)
        else:
            if len(q) > 0:
                q.pop()
    return ''.join(list(q))


if __name__ == "__main__":
    solution = Solution()

    #s1 = "ab#c"
    #s1 = "ab##"
    #s1 = "a##c"
    s1 = "a#c"
    print("\n s1: ", s1)

    #s2 = "ad#c"
    #s2 = "c#d#"
    #s2 = "#a#c"
    s2 = "b"
    print(" s2: ", s2)

    result = solution.backspaceCompare(s1, s2)
    print("\n result: ", result)
