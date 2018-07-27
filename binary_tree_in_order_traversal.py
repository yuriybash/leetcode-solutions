"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "TreeNode <{}>".format(self.val)

class Solution(object):
    def in_order_traversal_rcrs(self, root):
        """
        in-order traversal of binary tree (recursive version)

        :param root: root node
        :type root: TreeNode
        :return: list of node values for in-order traversal
        """
        node_vals = []
        if not root:
            return node_vals

        if(root.left):
            node_vals.extend(self.in_order_traversal_rcrs(root.left))
        node_vals.append(root.val)
        if(root.right):
            node_vals.extend(self.in_order_traversal_rcrs(root.right))

        return node_vals

    def in_order_traversal_iter(self, root):
        """
        in-order traversal of binary tree (iterative version)

        :param root: the tree (referenced by root)
        :type root: TreeNode
        :return: in-order traversal (of node values)
        :rtype: [int]
        """

        final_order, stack = [], []
        curr_node = root
        done = False

        while(not done):
            if curr_node.left:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                final_order.append(curr_node.val)
                if stack:
                    curr_node = stack.pop()
                    final_order.append(curr_node.val)
                    curr_node = curr_node.right
                else:
                    done = True

        return final_order
