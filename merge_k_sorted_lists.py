import heapq

# Definition for singly-linked list.
class ListNode(object):

    def __repr__(self):
        return "ListNode <%s>" % self.val

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        storage = []
        heapq.heapify(storage)
        for node in lists:
            while node:
                heapq.heappush(storage, node.val)
                node = node.next

        if not storage:
            return

        new_head = prev_node = ListNode(heapq.heappop(storage))
        while storage:
            new_node_to_add = ListNode(heapq.heappop(storage))
            prev_node.next = new_node_to_add
            prev_node = new_node_to_add

        return new_head


a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f

g = ListNode(2)
h = ListNode(6)
g.next = h

Solution().mergeKLists([a, d, g])
