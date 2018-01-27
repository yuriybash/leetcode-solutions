class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        start_node = l1 if l1.val <= l2.val else l2
        if(start_node == l1):
            l1 = l1.next
        else:
            l2 = l2.next
        curr_node = start_node
        while(l1 or l2):
            if not l1:
                curr_node.next = l2
                break
            elif not l2:
                curr_node.next = l1
                break
            else:
                l1_smaller = (l1.val <= l2.val)
                temp = l1 if l1_smaller else l2
                curr_node.next = temp
                curr_node = curr_node.next
                if l1_smaller:
                    l1 = l1.next
                else:
                    l2 = l2.next
        return start_node
