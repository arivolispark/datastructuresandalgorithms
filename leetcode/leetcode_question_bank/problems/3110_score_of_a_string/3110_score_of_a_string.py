import math

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        map = {}

        map['a'] = 97
        map['b'] = 98
        map['c'] = 99
        map['d'] = 100
        map['e'] = 101
        map['f'] = 102
        map['g'] = 103
        map['h'] = 104
        map['i'] = 105
        map['j'] = 106
        map['k'] = 107
        map['l'] = 108
        map['m'] = 109
        map['n'] = 110
        map['o'] = 111
        map['p'] = 112
        map['q'] = 113
        map['r'] = 114
        map['s'] = 115
        map['t'] = 116
        map['u'] = 117
        map['v'] = 118
        map['w'] = 119
        map['x'] = 120
        map['y'] = 121
        map['z'] = 122

        if s:
            for i in range(1, len(s)):
                score += abs(map[s[i-1]] - map[s[i]])
        return score
