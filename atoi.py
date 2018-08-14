import re

class Solution(object):
    def myAtoi(self, str_i):
        if not re.search('^[ ]*[+-]?[\d]+', str_i):
            return 0

        while str_i.startswith(" "):
            str_i = str_i.lstrip(" ")

        multiplier = 1
        if str_i.startswith("+") or str_i.startswith("-"):
            multiplier = 1 if str_i.startswith("+") else -1
            str_i = str_i[1:]
        parsed = multiplier * long(re.match('[\d]+', str_i).group())

        if parsed > 2**31-1:
            return 2**31-1
        elif parsed < -2**31:
            return -(2**31)
        else:
            return parsed
