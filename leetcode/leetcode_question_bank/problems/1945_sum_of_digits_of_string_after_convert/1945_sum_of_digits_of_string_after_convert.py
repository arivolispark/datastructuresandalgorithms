"""
Title:  1945. Sum of Digits of String After Convert

You are given a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the
alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform
the integer by replacing it with the sum of its digits. Repeat the transform
operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by
the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.



Example 1:
Input: s = "iiii", k = 1
Output: 36
Explanation: The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.


Example 2:
Input: s = "leetcode", k = 2
Output: 6
Explanation: The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.


Example 3:
Input: s = "zbax", k = 2
Output: 8


Constraints:
1) 1 <= s.length <= 100
2) 1 <= k <= 10
3) s consists of lowercase English letters.

"""


class Solution:

    def getLucky(self, s: str, k: int) -> int:
        answer = 0

        map = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 1,
            11: 2,
            12: 3,
            13: 4,
            14: 5,
            15: 6,
            16: 7,
            17: 8,
            18: 9,
            19: 10,
            20: 2,
            21: 3,
            22: 4,
            23: 5,
            24: 6,
            25: 7,
            26: 8
        }
        # print(" map: ", map)

        for i in range(len(s)):
            answer += map[ord(s[i]) + 1 - ord('a')]

        k -= 1
        if k == 0:
            return answer

        while k > 0:
            answer = get_digit_sum(answer)
            k -= 1
        return answer


def get_digit_sum(num: int):
    result = 0
    while num > 0:
        result += (num % 10)
        num //= 10
    return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.getLucky("iiii", 1), 36)
    test(solution.getLucky("leetcode", 2), 6)
    test(solution.getLucky("zbax", 2), 8)
    test(solution.getLucky("hvmhoasabaymnmsd", 1), 79)
