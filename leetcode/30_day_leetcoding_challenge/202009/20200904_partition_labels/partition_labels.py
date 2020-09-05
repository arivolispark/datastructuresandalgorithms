"""
Title:  Partition Labels

A string S of lowercase English letters is given. We want to partition this
string into as many parts as possible so that each letter appears in at most
one part, and return a list of integers representing the size of these parts.



Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.



Note:
1) S will have length in range [1, 500].
2) S will consist of lowercase English letters ('a' to 'z') only.

"""


from typing import List


class Solution:

    def partitionLabels(self, S: str) -> List[int]:
        end_idx = [0] * 26
        for i in range(len(S)):
            end_idx[ord(S[i]) - ord('a')] = i

        result = []
        start, end = 0, 0

        for i in range(len(S)):
            end = max(end, end_idx[ord(S[i]) - ord('a')])
            if i == end:
                result.append(i - start + 1)
                start = i + 1
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.partitionLabels("ababcbacadefegdehijhklij"), [9,7,8])
