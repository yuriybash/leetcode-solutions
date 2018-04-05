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


        left_most = -1
        start = 0
        end = None

        while True:
            idx_found = bin_search(nums, target, start=start, end=end)
            if idx_found != -1:
                left_most = idx_found
                start = 0
                end = idx_found-1
            else:
                break

                left_most = -1

        if left_most == -1:
            return [-1, -1]


        right_most = -1
        start = 0
        end = None

        while True:
            idx_found = bin_search(nums, target, start=start, end=end)
            if idx_found != -1:
                right_most = idx_found
                start = idx_found+1
                end = None
            else:
                break

        return [left_most, right_most]
