# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_to_index = {num: i for i, num in enumerate(postorder)}

        def build(pre_start: int, pre_end: int, post_start: int, post_end: int) -> TreeNode | None:
            if pre_start > pre_end:
                return None
            if pre_start == pre_end:
                return TreeNode(preorder[pre_start])

            rootVal = preorder[pre_start]
            leftRootVal = preorder[pre_start + 1]
            leftRootPostIndex = post_to_index[leftRootVal]
            leftSize = leftRootPostIndex - post_start + 1

            root = TreeNode(rootVal)
            root.left = build(pre_start + 1, pre_start + leftSize, post_start, leftRootPostIndex)
            root.right = build(pre_start + leftSize + 1, pre_end, leftRootPostIndex + 1, post_end - 1)
            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
