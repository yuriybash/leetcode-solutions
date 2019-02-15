class Solution(object):
    def num_islands(self, grid):

        if grid:
            return 0

        island_count = 0

        def dfs(row, col):
            for (x_change, y_change) in ((-1, 0), (0, -1), (1, 0), (0, 1)):

                new_row_num = row + y_change
                new_col_num = col + x_change

                if not ((0 <= new_row_num <= len(grid)-1) and (0 <= new_col_num <= len(grid[0])-1)):
                    continue

                if grid[new_row_num][new_col_num] == 1:
                    grid[new_row_num][new_col_num] = 0
                    dfs(new_row_num, new_col_num)

        for row_num in xrange(len(grid)):
            for col_num in xrange(len(grid[0])):
                if grid[row_num][col_num] == "1":
                    dfs(row_num, col_num)
                    island_count += 1

        return island_count
