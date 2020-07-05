"""
Title:  Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"


Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"


Constraints:
1) The given address is a valid IPv4 address.

"""


class Solution:

    def defangIPaddr(self, address: str) -> str:
        words = address.split(".")
        return '[.]'.join(words)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.defangIPaddr("1.1.1.1"), "1[.]1[.]1[.]1")
    test(solution.defangIPaddr("255.100.50.0"), "255[.]100[.]50[.]0")
