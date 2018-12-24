class Solution(object):

    def search(self, arr, target):

        if not arr:
            return -1

        def find_rot():
            lo = 0
            high = len(arr)-1

            while lo < high:
                mid = (lo + high) / 2

                if arr[mid] > arr[high]:
                    lo = mid + 1
                else:
                    high = mid
            return high

        def bin_search(subarray):
            lo = 0
            high = len(subarray) - 1

            while lo <= high:

                midpoint = (lo + high) / 2

                if subarray[midpoint] == target:
                    return midpoint
                elif subarray[midpoint] < target:
                    lo = midpoint + 1
                elif subarray[midpoint] > target:
                    high = midpoint - 1

            return -1

        rot = find_rot()
        if arr[rot] <= target <= arr[-1]:
            idx_found = bin_search(arr[rot:])
            if idx_found == -1:
                return -1
            else:
                return rot + idx_found
        else:
            return bin_search(arr[:rot])
