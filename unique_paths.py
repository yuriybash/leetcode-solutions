# Definition for singly-linked list.
class ListNode(object):

    def __repr__(self):
        return "ListNode <%s>" % self.val

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node_1_vals = []
        node_2_vals = []
        node = l1
        while node:
            node_1_vals.append(node.val)
            node = node.next

        node = l2
        while node:
            node_2_vals.append(node.val)
            node = node.next

        n1 = 0
        base = 1
        for digit in node_1_vals:
            n1 += digit * base
            base *= 10
        n2 = 0
        base = 1
        for digit in node_2_vals:
            n2 += digit * base
            base *= 10
        
        sum_ = list(str(n1 + n2))
        sum_.reverse()
        print sum_


        head = ListNode(int(sum_.pop(0)))
        prev = head
        for val in sum_:
            prev.next = ListNode(int(val))
            prev = prev.next
        return head






first = ListNode(2)
second = ListNode(4)
third = ListNode(3)
first.next = second
second.next= third

fourth = ListNode(5)
fifth = ListNode(6)
sixth = ListNode(4)
fourth.next = fifth
fifth.next = sixth

