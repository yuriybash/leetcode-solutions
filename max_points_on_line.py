from fractions import Fraction
from itertools import combinations, chain


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)


class Solution(object):
    def maxPoints(self, points):
        """
        Find max. num of points on a straight line given a set of points.

        :param points: the points
        :type points: list<Point>
        :return: max num pof points
        :rtype: int
        """
        unique_pts = {(pt.x, pt.y): pt for pt in points}.values()
        num_dupes = len(points) - len(unique_pts)
        if(len(unique_pts) <= 2):
            return len(unique_pts) + num_dupes

        max_pts_on_line = 0
        for i in range(len(unique_pts) - 1):

            first_pt, second_pt = unique_pts[i], unique_pts[i + 1]

            pts_on_line = 2
            for pt in unique_pts[0:i] + unique_pts[i + 2:]:

                if self._point_on_line(
                    first_pt, second_pt, pt, vertical=(
                        first_pt.x - second_pt.x == 0)):
                    pts_on_line += 1

            if pts_on_line > max_pts_on_line:
                max_pts_on_line = pts_on_line

        return max_pts_on_line + num_dupes

    def _point_on_line(self, fixed_pt_1, fixed_pt_2, test_pt, vertical=False):

        if vertical:
            return test_pt.x == fixed_pt_1.x

        m = Fraction(fixed_pt_1.y - fixed_pt_2.y, fixed_pt_1.x - fixed_pt_2.x)
        b = fixed_pt_1.y - m * fixed_pt_1.x
        if (test_pt.y == m * test_pt.x + b):
            return True


assert(Solution().maxPoints([Point(1, 1), Point(2, 2), Point(3, 3)]) == 3)

assert((Solution().maxPoints([
    Point(1, 1),
    Point(3, 2),
    Point(5, 3),
    Point(4, 1),
    Point(2, 3),
    Point(1, 4)])) == 4)

assert(Solution().maxPoints([Point(4, 0), Point(4, -1), Point(4, 5)]) == 3)

assert(Solution().maxPoints([Point(0, 0), Point(1, 1), Point(1, -1)]) == 2)

assert(Solution().maxPoints([Point(1, 1), Point(1, 1), Point(2, 3)]) == 3)

assert(Solution().maxPoints([Point(0, 0), Point(1, 1), Point(0, 0)]) == 3)

assert(Solution().maxPoints([Point(1, 1), Point(1, 1), Point(1, 1)]) == 3)

assert(Solution().maxPoints([Point(1, 1), Point(2, 2), Point(3, 3)]) == 3)

assert((Solution().maxPoints([
    Point(1, 1),
    Point(3, 2),
    Point(5, 3),
    Point(4, 1),
    Point(2, 3),
    Point(1, 4)])) == 4)

assert(Solution().maxPoints([Point(4, 0), Point(4, -1), Point(4, 5)]) == 3)

assert(Solution().maxPoints([Point(0, 0), Point(1, 1), Point(1, -1)]) == 2)

assert(Solution().maxPoints([Point(1, 1), Point(1, 1), Point(2, 3)]) == 3)

assert(Solution().maxPoints([Point(0, 0), Point(1, 1), Point(0, 0)]) == 3)

assert(Solution().maxPoints([Point(1, 1), Point(1, 1), Point(1, 1)]) == 3)
