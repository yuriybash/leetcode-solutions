# Definition for singly-linked list.
class ListNode(object):

    def __repr__(self):
        return "ListNode <%s>" % self.val

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        node = head
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev



# 1->2->3->4->5->NULL

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

x = Solution().reverseList(a)
print x.next.next.next.next.next