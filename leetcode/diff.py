"""
    Problem: Diff
    In this problem, you are given two strings, s1 and s2. s2 is a permutation
    of s1 along with one additional character in it. Find that extra character
    in s2. All the chars will be lower case.

    Example:
    Input: s1 = "xyz", s2 = "zaxy"
    Output: "a"
"""


def diff(s1, s2):
    i, j = len(s1), len(s2)

    result = []
    if i > j:
        for k in range(i):
            result.append(s1[k])

        for k in range(j):
            if s2[k] in result:
                result.remove(s2[k])
    else:
        for k in range(j):
            result.append(s2[k])
        for k in range(i):
            if s1[k] in result:
                result.remove(s1[k])

    return result[-1]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':

    testcases = [
                 ('xyz', 'zaxy', 'a'),
                 ('aabcd', 'bdacaa', 'a'),
                 ('fit', 'tiff', 'f')
                ]

    for t in testcases:
        test(diff(t[0], t[1]), t[-1])

