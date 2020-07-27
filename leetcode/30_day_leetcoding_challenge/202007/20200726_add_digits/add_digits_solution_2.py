"""
Title:  Add Digits

Given a non-negative integer num, repeatedly add all its digits
until the result has only one digit.


Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.



Follow up:
Could you do it without any loop/recursion in O(1) runtime?

"""


class Solution:

    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.addDigits(0), 0)
    test(solution.addDigits(1), 1)
    test(solution.addDigits(2), 2)
    test(solution.addDigits(3), 3)
    test(solution.addDigits(4), 4)
    test(solution.addDigits(5), 5)
    test(solution.addDigits(6), 6)
    test(solution.addDigits(7), 7)
    test(solution.addDigits(8), 8)
    test(solution.addDigits(9), 9)

    test(solution.addDigits(10), 1)
    test(solution.addDigits(11), 2)
    test(solution.addDigits(12), 3)
    test(solution.addDigits(13), 4)
    test(solution.addDigits(14), 5)
    test(solution.addDigits(15), 6)
    test(solution.addDigits(16), 7)
    test(solution.addDigits(17), 8)
    test(solution.addDigits(18), 9)
    test(solution.addDigits(19), 1)

    test(solution.addDigits(20), 2)
    test(solution.addDigits(21), 3)
    test(solution.addDigits(22), 4)
    test(solution.addDigits(23), 5)
    test(solution.addDigits(24), 6)
    test(solution.addDigits(25), 7)
    test(solution.addDigits(26), 8)
    test(solution.addDigits(27), 9)
    test(solution.addDigits(28), 1)
    test(solution.addDigits(29), 2)

    test(solution.addDigits(30), 3)
    test(solution.addDigits(31), 4)
    test(solution.addDigits(32), 5)
    test(solution.addDigits(33), 6)
    test(solution.addDigits(34), 7)
    test(solution.addDigits(35), 8)
    test(solution.addDigits(36), 9)
    test(solution.addDigits(37), 1)
    test(solution.addDigits(38), 2)
    test(solution.addDigits(39), 3)

    test(solution.addDigits(40), 4)
    test(solution.addDigits(41), 5)
    test(solution.addDigits(42), 6)
    test(solution.addDigits(43), 7)
    test(solution.addDigits(44), 8)
    test(solution.addDigits(45), 9)
    test(solution.addDigits(46), 1)
    test(solution.addDigits(47), 2)
    test(solution.addDigits(48), 3)
    test(solution.addDigits(49), 4)

    test(solution.addDigits(50), 5)
    test(solution.addDigits(51), 6)
    test(solution.addDigits(52), 7)
    test(solution.addDigits(53), 8)
    test(solution.addDigits(54), 9)
    test(solution.addDigits(55), 1)
    test(solution.addDigits(56), 2)
    test(solution.addDigits(57), 3)
    test(solution.addDigits(58), 4)
    test(solution.addDigits(59), 5)

    test(solution.addDigits(60), 6)
    test(solution.addDigits(61), 7)
    test(solution.addDigits(62), 8)
    test(solution.addDigits(63), 9)
    test(solution.addDigits(64), 1)
    test(solution.addDigits(65), 2)
    test(solution.addDigits(66), 3)
    test(solution.addDigits(67), 4)
    test(solution.addDigits(68), 5)
    test(solution.addDigits(69), 6)

    test(solution.addDigits(70), 7)
    test(solution.addDigits(71), 8)
    test(solution.addDigits(72), 9)
    test(solution.addDigits(73), 1)
    test(solution.addDigits(74), 2)
    test(solution.addDigits(75), 3)
    test(solution.addDigits(76), 4)
    test(solution.addDigits(77), 5)
    test(solution.addDigits(78), 6)
    test(solution.addDigits(79), 7)

    test(solution.addDigits(80), 8)
    test(solution.addDigits(81), 9)
    test(solution.addDigits(82), 1)
    test(solution.addDigits(83), 2)
    test(solution.addDigits(84), 3)
    test(solution.addDigits(85), 4)
    test(solution.addDigits(86), 5)
    test(solution.addDigits(87), 6)
    test(solution.addDigits(88), 7)
    test(solution.addDigits(89), 8)

    test(solution.addDigits(90), 9)
    test(solution.addDigits(91), 1)
    test(solution.addDigits(92), 2)
    test(solution.addDigits(93), 3)
    test(solution.addDigits(94), 4)
    test(solution.addDigits(95), 5)
    test(solution.addDigits(96), 6)
    test(solution.addDigits(97), 7)
    test(solution.addDigits(98), 8)
    test(solution.addDigits(99), 9)

    test(solution.addDigits(100), 1)
    test(solution.addDigits(101), 2)
    test(solution.addDigits(102), 3)
    test(solution.addDigits(103), 4)
    test(solution.addDigits(104), 5)
    test(solution.addDigits(105), 6)
    test(solution.addDigits(106), 7)
    test(solution.addDigits(107), 8)
    test(solution.addDigits(108), 9)
    test(solution.addDigits(109), 1)

    test(solution.addDigits(110), 2)
    test(solution.addDigits(111), 3)
    test(solution.addDigits(112), 4)
    test(solution.addDigits(113), 5)
    test(solution.addDigits(114), 6)
    test(solution.addDigits(115), 7)
    test(solution.addDigits(116), 8)
    test(solution.addDigits(117), 9)
    test(solution.addDigits(118), 1)
    test(solution.addDigits(119), 2)

    test(solution.addDigits(120), 3)
    test(solution.addDigits(121), 4)
    test(solution.addDigits(122), 5)
    test(solution.addDigits(123), 6)
    test(solution.addDigits(124), 7)
    test(solution.addDigits(125), 8)
    test(solution.addDigits(126), 9)
    test(solution.addDigits(127), 1)
    test(solution.addDigits(128), 2)
    test(solution.addDigits(129), 3)

    test(solution.addDigits(130), 4)
    test(solution.addDigits(131), 5)
    test(solution.addDigits(132), 6)
    test(solution.addDigits(133), 7)
    test(solution.addDigits(134), 8)
    test(solution.addDigits(135), 9)
    test(solution.addDigits(136), 1)
    test(solution.addDigits(137), 2)
    test(solution.addDigits(138), 3)
    test(solution.addDigits(139), 4)

    test(solution.addDigits(140), 5)
    test(solution.addDigits(141), 6)
    test(solution.addDigits(142), 7)
    test(solution.addDigits(143), 8)
    test(solution.addDigits(144), 9)
    test(solution.addDigits(145), 1)
    test(solution.addDigits(146), 2)
    test(solution.addDigits(147), 3)
    test(solution.addDigits(148), 4)
    test(solution.addDigits(149), 5)

    test(solution.addDigits(150), 6)
    test(solution.addDigits(151), 7)
    test(solution.addDigits(152), 8)
    test(solution.addDigits(153), 9)
    test(solution.addDigits(154), 1)
    test(solution.addDigits(155), 2)
    test(solution.addDigits(156), 3)
    test(solution.addDigits(157), 4)
    test(solution.addDigits(158), 5)
    test(solution.addDigits(159), 6)

    test(solution.addDigits(160), 7)
    test(solution.addDigits(161), 8)
    test(solution.addDigits(162), 9)
    test(solution.addDigits(163), 1)
    test(solution.addDigits(164), 2)
    test(solution.addDigits(165), 3)
    test(solution.addDigits(166), 4)
    test(solution.addDigits(167), 5)
    test(solution.addDigits(168), 6)
    test(solution.addDigits(169), 7)

    test(solution.addDigits(170), 8)
    test(solution.addDigits(171), 9)
    test(solution.addDigits(172), 1)
    test(solution.addDigits(173), 2)
    test(solution.addDigits(174), 3)
    test(solution.addDigits(175), 4)
    test(solution.addDigits(176), 5)
    test(solution.addDigits(177), 6)
    test(solution.addDigits(178), 7)
    test(solution.addDigits(179), 8)

    test(solution.addDigits(180), 9)
    test(solution.addDigits(181), 1)
    test(solution.addDigits(182), 2)
    test(solution.addDigits(183), 3)
    test(solution.addDigits(184), 4)
    test(solution.addDigits(185), 5)
    test(solution.addDigits(186), 6)
    test(solution.addDigits(187), 7)
    test(solution.addDigits(188), 8)
    test(solution.addDigits(189), 9)

    test(solution.addDigits(190), 1)
    test(solution.addDigits(191), 2)
    test(solution.addDigits(192), 3)
    test(solution.addDigits(193), 4)
    test(solution.addDigits(194), 5)
    test(solution.addDigits(195), 6)
    test(solution.addDigits(196), 7)
    test(solution.addDigits(197), 8)
    test(solution.addDigits(198), 9)
    test(solution.addDigits(199), 1)

    test(solution.addDigits(200), 2)
    test(solution.addDigits(201), 3)
    test(solution.addDigits(202), 4)
    test(solution.addDigits(203), 5)
    test(solution.addDigits(204), 6)
    test(solution.addDigits(205), 7)
    test(solution.addDigits(206), 8)
    test(solution.addDigits(207), 9)
    test(solution.addDigits(208), 1)
    test(solution.addDigits(209), 2)

    test(solution.addDigits(210), 3)
    test(solution.addDigits(211), 4)
    test(solution.addDigits(212), 5)
    test(solution.addDigits(213), 6)
    test(solution.addDigits(214), 7)
    test(solution.addDigits(215), 8)
    test(solution.addDigits(216), 9)
    test(solution.addDigits(217), 1)
    test(solution.addDigits(218), 2)
    test(solution.addDigits(219), 3)

    test(solution.addDigits(220), 4)
    test(solution.addDigits(221), 5)
    test(solution.addDigits(222), 6)
    test(solution.addDigits(223), 7)
    test(solution.addDigits(224), 8)
    test(solution.addDigits(225), 9)
    test(solution.addDigits(226), 1)
    test(solution.addDigits(227), 2)
    test(solution.addDigits(228), 3)
    test(solution.addDigits(229), 4)
