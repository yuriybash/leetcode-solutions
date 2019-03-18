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


class Tree(object):

    def __repr__(self):

        return "Tree <%s>" % self.val

    def __init__(self, val, children=None):
        self.val = val
        self.children = children or []

    def dfs(self, val_to_find, seen=None):

        seen = seen or []

        if self.val == val_to_find:
            return self

        for child in self.children:
            if child in seen:
                continue
            target_node = child.dfs(val_to_find, seen=seen+[child])
            if target_node:
                return target_node
        return None

    def bfs(self, val_to_find):

        seen = []
        queue = [self]

        while queue:
            node = queue.pop()
            if node in seen:
                continue
            seen.append(node)
            if node.val == val_to_find:
                return node
            for child in node.children:
                queue.append(child)

class SLinkedList(object):

    def __repr__(self):
        return "<%s %s> " % (self.__class__.__name__, self.val)

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = None

    def add(self, node_to_add):

        if not isinstance(node_to_add, SLinkedList):
            node_to_add = SLinkedList(node_to_add)

        self.next_ = node_to_add

    def find(self, val_to_find):

        node = self
        while node:
            if node.val == val_to_find:
                return node
            node = node.next_

class DLinkedList(SLinkedList):

    def __init__(self, val, next_=None, prev=None):
        self.prev = prev
        super(DLinkedList, self).__init__(val, next_=next_)

    def add(self, val):

        node = val if isinstance(val, DLinkedList) else DLinkedList(val)
        node.prev = self
        self.next_ = node

class Stack(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.curr_size = 0


    def push(self, val):

        if self.curr_size + 1 > self.capacity:
            raise ValueError("stack full")

        self.storage.append(val)
        self.curr_size += 1

    def peek(self):

        return self.storage[-1]

    def pop(self):
        if not self.curr_size:
            return
        
        self.curr_size -= 1
        return self.storage.pop()


def bin_search(arr, target):

    low, high = 0, len(arr)-1
    while low <= high:

        midpoint = (low + high) / 2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            low = midpoint+1
        else:
            high = midpoint-1

    print "low: ", low
    print "high: ", high




print bin_search([0, 1, 2, 2, 3, 4, 5, 7, 7, 8, 10], )















