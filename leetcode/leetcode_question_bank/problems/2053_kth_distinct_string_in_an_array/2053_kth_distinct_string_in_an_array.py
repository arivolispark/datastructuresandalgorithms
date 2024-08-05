"""
Title:  2053. Kth Distinct String in an Array

A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct
string present in arr. If there are fewer than k distinct strings, return
an empty string "".

Note that the strings are considered in the order in which they appear in the array.



Example 1:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned.


Example 2:
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.


Example 3:
Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".


Constraints:
1) 1 <= k <= arr.length <= 1000
2) 1 <= arr[i].length <= 5
3) arr[i] consists of lowercase English letters.
"""

from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map = {}
        result = []
        length = len(arr)

        for i in range(length):
            map[arr[i]] = map.get(arr[i], 0) + 1

        for i in range(length):
            if arr[i] in map and map[arr[i]] == 1:
                result.append(arr[i])

        if len(result) < k:
            return ""
        return result[k - 1]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.kthDistinct(["d","b","c","b","c","a"], 2), "a")
    test(solution.kthDistinct(["aaa","aa","a"], 1), "aaa")
    test(solution.kthDistinct(["a","b","a"], 3), "")
    test(solution.kthDistinct(["c","exjk","nbmg","kgnas","s","oydx","ghpao","c","r","ohdm","fq","ashgg","mm","cc","mymy","w","t","neb","grjdb","cukk","ujyhn","dq","hhuo","qu","seslw","ybulz","iug","rs","kyfu","krz","nw","txnn","r","zpuao","sh","rfc","c","hgr","jfia","egm","gmuuv","gh","x","nfvgv","ibo","al","wn","o","dyu","zgkk","gdzrf","m","ui","xwsj","zeld","muowr","d","xgiu","yfu"], 19), "dq")
