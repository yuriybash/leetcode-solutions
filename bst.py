import sys

class TreeNode(object):

    def __repr__(self):
        return "<TreeNode %s>" % self.val

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, node_to_add):

        if isinstance(node_to_add, int):
            node_to_add = TreeNode(node_to_add)

        if node_to_add.val == self.val:
            raise ValueError("cannot be equal")

        if node_to_add.val > self.val:
            if not self.right:
                self.right = node_to_add
            else:
                self.right.add(node_to_add)
            return


        if node_to_add.val < self.val:
            if not self.left:
                self.left = node_to_add
            else:
                self.left.add(node_to_add)
            return

    def find(self, val):

        if self.val == val:
            return True

        if val < self.val:
            if not self.left:
                return False
            return self.left.find(val)

        if val > self.val:
            if not self.right:
                return False
            return self.right.find(val)

    def is_valid(self, min_=-(sys.maxint)-1, max_=sys.maxint):

        if self.val > max_ or self.val < min_:
            return False

        left_valid = True if not self.left else self.left.is_valid(min_=min_, max_=self.val)
        right_valid = True if not self.right else self.right.is_valid(min_=self.val, max_=max_)
        return left_valid and right_valid


root = TreeNode(10)
root.add(5)
root.add(7)
root.add(12)
root.add(11)
root.add(111)
root.add(112)

print root.is_valid()





