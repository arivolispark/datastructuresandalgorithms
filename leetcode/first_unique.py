# First Unique
# Given a string containing all lowercase characters, find
# the first non-repeating character in the string

# Example 1
# Input : "trignometry"
# Output: "i"

# Example 2
# Input : "abccba"
# Output: ""


def first_unique(s):
    """
    Time:  O(n)
    """

    char_freq_map = {}

    if s:
        n = len(s)
        for i in range(n):
            char_freq_map[s[i]] = char_freq_map.get(s[i], 0) + 1

        for i in range(n):
            if char_freq_map.get(s[i]) == 1:
                return s[i]
    return ""


def first_unique_1(s):
    """
    Time:  O(n^2)
    """

    l = []
    for x in s:
        k = s.count(x)
        if k == 1:
            l.append(x)
    if len(l) == 0:
        return ""
    else:
        return l[0]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    test_cases = [('himanshu sharma', 'i'),
                  ('abccba', ''),
                  ('successful', 'e')
		 ]
    for t in test_cases:
        test(first_unique(t[0]), t[1])