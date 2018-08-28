from collections import OrderedDict

class Solution(object):

    MAP = OrderedDict(
        [(1000, 'M'),
         (900, 'CM'),
         (500, 'D'),
         (400, 'CD'),
         (100, 'C'),
         (90, 'XC'),
         (50, 'L'),
         (40, 'XL'),
         (10, 'X'),
         (9, 'IX'),
         (5, 'V'),
         (4, 'IV'),
         (1, 'I')]
    )

    def intToRoman(self, num):

        answer = ""
        for k, v in self.MAP.items():
            quotient, remainder = (num / k), (num % k)
            if quotient:
                answer += quotient * v
                num = remainder
        return answer
