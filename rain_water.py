class Solution(object):
    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        total = 0

        maxes_from_left = {0: heights[0]}
        maxes_from_right = {len(heights)-1: heights[-1]}

        for idx in xrange(1, len(heights)):
            maxes_from_left[idx] = max(heights[idx], maxes_from_left[idx-1])

        for idx in xrange(len(heights)-2, -1, -1):
            maxes_from_right[idx] = max(heights[idx], maxes_from_right[idx + 1])

        for idx in xrange(len(heights)):
            max_left = maxes_from_left[idx]
            max_right = maxes_from_right[idx]
            total += min(max_left, max_right) - heights[idx]
        return total



#     idx: 0  1  2  3  4  5  6  7  8  9 10 11
input_1 = [0,1,0,2,1,0,1,3,2,1,2,1]

print Solution().trap(input_1)