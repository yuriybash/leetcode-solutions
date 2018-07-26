"""
In a 2 dimensional array grid, each value grid[i][j] represents the height of
a building located there. We are allowed to increase the height of any number
of buildings, by any amount (the amounts can be different for different
buildings). Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid,
i.e. top, bottom, left, and right, must be the same as the skyline of the
original grid. A city's skyline is the outer contour of the rectangles formed
by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be
increased?
"""


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):

        rotated = zip(*grid[::-1])  # to avoid O(n^2)
        n = len(grid)

        height_increase = 0
        for row_idx, current_row in enumerate(grid):
            for col_idx, elem in enumerate(current_row):
                max_row = max(current_row)
                max_col = max(rotated[n - 1 - col_idx])
                new_height = min(max_row, max_col)
                height_increase += new_height - elem

        return height_increase

    def _matrix_rotate_90_cc(self, matrix):
        """
        Rotate a matrix counterclockwise 90 degrees (not in place)

        :param matrix: the matrix. list of lists.
        :type: <List<List>>
        :return: the rotated (new) matrix
        :rtype: <List<List>>
        """
        n = len(matrix)
        rotated = [[None for _ in range(n)] for _ in range(n)]
        for row_idx in range(len(matrix) - 1):
            for col_idx, elem in enumerate(matrix[row_idx]):
                rotated[n - 1 - col_idx][row_idx] = elem
        return rotated
