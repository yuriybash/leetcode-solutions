"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def in_order_traversal(self, root):
        """
        in-order traversal of binary tree

        :param root: root node
        :type root: TreeNode
        :return: list of node values for in-order traversal
        """
        node_vals = []
        if not root:
            return node_vals

        if(root.left):
            node_vals.extend(self.in_order_traversal(root.left))
        node_vals.append(root.val)
        if(root.right):
            node_vals.extend(self.in_order_traversal(root.right))

        return node_vals
