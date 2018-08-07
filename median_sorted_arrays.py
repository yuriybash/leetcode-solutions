class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        credit to https://leetcode.com/articles/median-of-two-sorted-arrays/
        implementation done as exercise

        i = # of elements in first array on left half of split
        j = # of elements in second array on left half of split
        m = total # of elements in first array
        n = total # of elements in second array

        given this, you get:

        i + j = m - i + n - j + 1 (add 1 for arithmetic convenience)

        and then

        j = ((m+n+1)/2) - i

        you keep bifurcating i on the range [i_min, i_max]
        """

        # reverse b/c n >= m, since 0<=i<=m and j = (m+n+1)/2-i
        if len(nums1) > len(nums2):
            self.m, self.n = len(nums2), len(nums1)
            a, b = nums2, nums1
        else:
            self.m, self.n = len(nums1), len(nums2)
            a, b = nums1, nums2

        i_min, i_max, halfway = 0, self.m, (self.m+self.n+1)/2

        while(i_min <= i_max):
            i = (i_min+i_max)/2
            j = halfway-i

            if i < self.m and b[j-1] > a[i]: # the current value of i is too small
                i_min = i+1
            elif i > 0 and a[i-1] > b[j]: # the current value of i is too big
                i_max = i-1
            else:
                # the current value of i is correct
                return self.determine_median_val(a, b, i, j)

    def determine_median_val(self, a, b, i, j):

        if i == 0: # all of A falls on right side of split
            max_of_left = b[j - 1]
        elif j == 0: # all of B falls on right side of split
            max_of_left = a[i - 1]
        else:
            max_of_left = max(a[i - 1], b[j - 1])

        if (self.m + self.n) % 2 == 1:
            return max_of_left

        if i == self.m: # all of A falls on left side of split
            min_of_right = b[j]
        elif j == self.n: # all of B falls on left side of split
            min_of_right = a[i]
        else:
            min_of_right = min(a[i], b[j])

        return (max_of_left + min_of_right) / 2.0
