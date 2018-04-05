class Solution(object):
    def searchRange(self, nums, target):

        def bin_search(arr, elem, start=0, end=None):

            if end is None:
                end = len(arr)-1
            if start > end:
                return -1

            midpoint = (start + end) / 2
            if arr[midpoint] == elem:
                return midpoint
            elif arr[midpoint] < elem:
                return bin_search(arr, elem, start=midpoint+1, end=end)
            elif elem < arr[midpoint]:
                return bin_search(arr, elem, start=start, end=midpoint-1)

        def find_left_or_right_position(arr, left_most):
            most = -1
            start = 0
            end = None

            while True:
                idx_found = bin_search(nums, target, start=start, end=end)
                if idx_found != -1:
                    most = idx_found

                    if left_most == 1:
                        start = 0
                        end = idx_found - 1
                    else:
                        start = idx_found + 1
                        end = None
                else:
                    break

            return most

        left_most = find_left_or_right_position(nums, 1)
        right_most = find_left_or_right_position(nums, 0)

        return [left_most, right_most]

print Solution().searchRange([5, 7,7,8,8,10], 8)
print Solution().searchRange([2, 2], 2)