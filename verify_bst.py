import sys

class Solution(object):

    def isValidBST(self, root):

        seen = set()
        
        def bst_verify(node, min_val=(-sys.maxint-1), max_val=sys.maxint):

            if not node:
                return

            if (node.val < min_val) or (node.val > max_val) or (node.val in seen):
                raise Exception
            seen.add(node.val)
            

            bst_verify(node.left, min_val=min_val, max_val=node.val)
            bst_verify(node.right, min_val=node.val, max_val=max_val)


        try:
            bst_verify(root)
        except Exception:https://releases.hashicorp.com/consul/1.4.2/consul_1.4.2_linux_amd64.zip
            return False

        return True
