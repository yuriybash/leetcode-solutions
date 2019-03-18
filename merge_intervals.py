# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        new_intervals = []

        for pair in sorted(intervals, key=lambda x: x.start):
            if new_intervals and new_intervals[-1].end >= pair.start:
                new_intervals[-1].end = max(new_intervals[-1].end, pair.end)
            else:
                new_intervals.append(pair)
        return new_intervals
