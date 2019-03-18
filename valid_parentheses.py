class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pairs = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        for char in s:
            if not stack:
                if char in pairs:
                    stack.append(char)
                else:
                    return False
            else:
                if char in pairs:
                    stack.append(char)
                else:
                    existing = stack.pop()
                    if pairs[existing] != char:
                        return False
        return not stack
