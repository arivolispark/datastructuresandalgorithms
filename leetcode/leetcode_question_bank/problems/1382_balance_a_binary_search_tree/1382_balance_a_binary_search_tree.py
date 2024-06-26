# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            if root is None:
                return
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)

        def build(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            mid = (start + end) >> 1
            l_bst = build(start, mid - 1)
            r_bst = build(mid + 1, end)
            return TreeNode(result[mid], l_bst, r_bst)

        result = []
        dfs(root)
        return build(0, len(result) - 1)
