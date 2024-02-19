# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: TreeNode, result: List[int]):
            if not root:
                return None
            result.append(root.val)
            dfs(root.left, result)
            dfs(root.right, result)

        result = []
        dfs(root, result)
        return result
