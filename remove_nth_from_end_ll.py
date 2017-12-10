# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "ListNode <{}>".format(self.val)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        storage = {}
        root = head
        idx = 0

        while(head):
            storage[idx] = head
            head = head.next
            idx += 1

        if len(storage) == n:
            return root.next

        storage[len(storage)-n-1].next = storage.get(len(storage)-n+1, None)
        return root
