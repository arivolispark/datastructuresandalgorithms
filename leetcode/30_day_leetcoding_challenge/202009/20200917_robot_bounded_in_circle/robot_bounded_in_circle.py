"""
Title: Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot
can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.


Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



Example 1:
Input: "GGLLGG"
Output: true
Explanation:
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.



Example 2:
Input: "GG"
Output: false
Explanation:
The robot moves north indefinitely.



Example 3:
Input: "GL"
Output: true
Explanation:
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


Note:
1) 1 <= instructions.length <= 100
2) instructions[i] is in {'G', 'L', 'R'}

"""


class Solution:

    def isRobotBounded(self, instructions: str) -> bool:
        visited = set()
        x = y = 0
        direction = 0

        visited.add((x, y, direction))
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        for _ in range(4):
            for instruction in instructions:
                if instruction == "L":
                    direction = (direction + 1) % 4
                elif instruction == "R":
                    direction = (direction - 1) % 4
                else:
                    dx, dy = directions[direction]
                    x += dx
                    y += dy
            if (x, y, direction) in visited:
                return True
            visited.add((x, y, direction))
        return False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.isRobotBounded("GGLLGG"), True)
    test(solution.isRobotBounded("GG"), False)
    test(solution.isRobotBounded("GL"), True)
