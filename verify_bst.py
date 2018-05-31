import sys

class TreeNode(object):

    def __repr__(self):
        return str(self.x)

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isValidBST(self, root):

        seen = set()
        def bst_verify(node, min_val=(-sys. maxint -1), max_val=sys.maxint):

            if not node:
                return

            if (node.val < min_val) or (node.val > max_val) or (node.val in seen):
                raise InvalidBst
            seen.add(node.val)

            bst_verify(node.left, min_val=min_val, max_val=node.val)
            bst_verify(node.right, min_val=node.val, max_val=max_val)

        try:
            bst_verify(root)
        except InvalidBst:
            return False

        return True


class InvalidBst(Exception):
    pass
