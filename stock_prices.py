import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_values = []
        min_so_far = sys.maxint

        for price in prices:
            min_values.append(min(min_so_far, price))
            min_so_far = min(min_so_far, price)

        max_values = []
        max_so_far = -(sys.maxint)-1
        for price in reversed(prices):
            max_values.insert(0, (max(max_so_far, price)))
            max_so_far = max(max_so_far, price)

        return max([max_values[i] - min_values[i] for i in xrange(len(max_values))])
