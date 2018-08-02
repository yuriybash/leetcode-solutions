class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Given a string s, find the length of the longest substring without
        repeating characters.

        :param s: input string
        :type s: str
        :return: longest substring
        :rtype: int
        """

        if not s:
            return 0

        max_length = i = j = 0
        chars = {}

        while(j < len(s)):
            if s[j] not in chars:
                chars[s[j]] = j
                if (j - i + 1) >= max_length:
                    max_length = j-i+1
            else:

                # have to reset characters to compare against
                for idx in range(i, chars[s[j]]+1):
                    char_at_idx = s[idx]
                    chars.pop(char_at_idx)

                chars[s[j]] = j

                # skip ahead to one past the index of the "new" duplicate
                i = chars[s[j]]+1
            j+=1
        return max_length
