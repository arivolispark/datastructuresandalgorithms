"""
Title:  Hamming Distance

The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.


Example:
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""


class Solution:

    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0

        xor_value = x ^ y
        while xor_value > 0:
            if xor_value & 1:
                hamming_distance += 1
            xor_value >>= 1

        return hamming_distance


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.hammingDistance(1, 4), 2)
