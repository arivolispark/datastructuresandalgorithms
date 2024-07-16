# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pathToStart = []
        pathToDestination = []

        dfs(root, startValue, pathToStart)
        dfs(root, destValue, pathToDestination)

        while pathToStart and pathToDestination and pathToStart[-1] == pathToDestination[-1]:
            pathToStart.pop()
            pathToDestination.pop()

        return 'U' * len(pathToStart) + ''.join(reversed(pathToDestination))


def dfs(root: Optional[TreeNode], val: int, path: List[chr]) -> bool:
    if root and root.val == val:
        return True

    if root.left and dfs(root.left, val, path):
        path.append('L')
    elif root.right and dfs(root.right, val, path):
        path.append('R')

    return len(path) > 0
