class Solution(object):

    mapped = {
        'I': 1,
        'IV': 4,
        'IX': 9,
        'V': 5,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    def romanToInt(self, s):

        total = 0
        for idx in xrange(len(s)):

            if idx >= 1 and (s[idx-1] + s[idx]) in self.mapped:
                continue
            elif idx < len(s)-1 and (s[idx]+s[idx+1]) in self.mapped:
                total += self.mapped[s[idx]+s[idx+1]]
            else:
                total += self.mapped[s[idx]]

        return total
