# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        TO_BE_DELETED = -1

        def postorder_traverse(node):
            if node is None:
                return

            postorder_traverse(node.left)
            if node.left is not None and node.left.val == TO_BE_DELETED:
                node.left = None

            postorder_traverse(node.right)
            if node.right is not None and node.right.val == TO_BE_DELETED:
                node.right = None

            if node.left is None and node.right is None and node.val == target:
                node.val = TO_BE_DELETED

        postorder_traverse(root)

        if root.val == TO_BE_DELETED:
            return None

        return root
