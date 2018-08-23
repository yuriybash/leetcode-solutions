"""
Given a string s, find the longest palindromic substring in s.
"""

class Solution(object):
    def longestPalindrome(self, s):

        if len(s) <= 1:
            return s

        # shortcut, executed quickly by cpython
        if len(s) * s[0] == s:
            return s

        longest = s[0]
        for idx, char in enumerate(s):
            for subsqnt_char in s[idx+1:]:
                char += subsqnt_char
                if char == char[::-1] and len(char) > len(longest):
                    longest = char
        return longest
