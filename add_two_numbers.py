import ast

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "ListNode <{}>".format(self.val)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        n1, n2 = [], []

        while(l1):
            n1.append(str(l1.val))
            l1 = l1.next

        while(l2):
            n2.append(str(l2.val))
            l2 = l2.next

        # must use literal_eval to account for values > max float
        sum = int(ast.literal_eval(
            ''.join(n1)[::-1])) + int(ast.literal_eval(''.join(n2)[::-1]))

        _reversed = ''.join(reversed(str(sum)))
        root = current_node = ListNode(_reversed[0])
        for digit in _reversed[1:]:
            current_node.next = ListNode(int(digit))
            current_node = current_node.next

        return root
