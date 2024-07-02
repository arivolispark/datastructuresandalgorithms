# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetric(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if a is None and b is None:
                return True
            elif a is None and b is not None:
                return False
            elif a is not None and b is None:
                return False
            elif a.val != b.val:
                return False
            
            return (a.val == b.val) and isSymmetric(a.left, b.right) and isSymmetric(a.right, b.left)

        return isSymmetric(root, root)
