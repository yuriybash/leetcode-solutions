# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return None

        copies = {}

        def inner(node):

            if not node:
                return

            if copies.get(node):
                return copies[node]

            copy = RandomListNode(node.label)
            copies[node] = copy
            copy.next = inner(node.next)
            copy.random = inner(node.random)
            return copy

        inner(head)
        return copies[head]
