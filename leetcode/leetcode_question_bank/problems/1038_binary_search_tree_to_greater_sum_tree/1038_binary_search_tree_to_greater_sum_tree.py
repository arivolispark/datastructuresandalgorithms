# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        inorder_list = []
        sum, cumulative_sum = 0, 0
        map = {}

        inorder_traversal(root, inorder_list)
        #print(" inorder_list: ", inorder_list)

        inorder_list.sort()
        #print(" inorder_list: ", inorder_list)

        for i in range(len(inorder_list)):
            sum += inorder_list[i]
        #print(" sum: ", sum)

        for i in range(len(inorder_list)):
            cumulative_sum += inorder_list[i]
            map[inorder_list[i]] = sum - cumulative_sum + inorder_list[i]
        #print(" map: ", map)

        inorder(root, map)
        return root
        

def inorder(root: TreeNode, map: dict):
    curr = root
    if curr:
        inorder(curr.left, map)
        inorder(curr.right, map)
        curr.val = map[curr.val]


def inorder_traversal(root: TreeNode, result: List[int]):
    curr = root
    if curr:
        inorder_traversal(curr.left, result)
        inorder_traversal(curr.right, result)
        result.append(curr.val)
