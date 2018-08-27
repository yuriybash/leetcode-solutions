class Solution(object):
    def maxArea(self, heights):

        max_area, left, right = 0, 0, len(heights) - 1
        while(left!=right):

            shorter, longer = right, left
            if heights[left] < heights[right]:
                shorter, longer = longer, shorter

            rect_area = (right-left) * heights[shorter]
            max_area = rect_area if rect_area > max_area else max_area

            if shorter == left:
                left+=1
            else:
                right-=1

        return max_area
