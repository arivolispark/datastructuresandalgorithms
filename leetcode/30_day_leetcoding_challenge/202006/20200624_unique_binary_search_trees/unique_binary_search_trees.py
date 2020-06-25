"""
Title:  Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?


Example 1:

Input: 3
Output: 5

Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3



Example 2:

Input: 1
Output: 1

Explanation:
Given n = 1, there is a total of 1 unique BST's:

   1


Example 3:

Input: 2
Output: 2

Explanation:
Given n = 2, there are total of 2 unique BST's:

   1         2
    \       /
    2      1



Example 4:

Input: 4
Output: 14

Explanation:
Given n = 2, there are total of 2 unique BST's:

 1            1            1            1            1
  \            \            \            \            \
  2             2            3            4            4
   \             \           / \         /             /
    3             4         2   4       2             3
     \           /                       \            /
      4         3                         3          2


   2            2
  / \          / \
 1  3         1   4
     \           /
     4          3


   3            3
  / \          / \
 1   4        2   4
  \          /
   2        1


       4            1            1            1            1
      /            \            \            \            \
     3             2            3            4            4
    /             \           / \         /             /
   2             4         2   4       2             3
  /   \           /                       \            /
 1         3                         3          2



"""


class Solution:

    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [0] * (n + 1)

        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] = dp[i] + dp[i - j] * dp[j - 1]

        return dp[n]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.numTrees(0), 1)
    test(solution.numTrees(1), 1)
    test(solution.numTrees(2), 2)
    test(solution.numTrees(3), 5)
    test(solution.numTrees(4), 14)
    test(solution.numTrees(5), 42)
