# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_value_to_node_map = {}
        children_value = set()

        for p, c, is_left in descriptions:
            parent_node = node_value_to_node_map.setdefault(p, TreeNode(p))
            child_node = node_value_to_node_map.setdefault(c, TreeNode(c))
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            children_value.add(c)
        root_value = (set(node_value_to_node_map) - set(children_value)).pop()
        return node_value_to_node_map[root_value]
