import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max = max_so_far = -sys.maxint-1
        for idx, num in enumerate(nums):
            if num > num + max_so_far:
                max_so_far = num
                global_max = max(max_so_far, global_max)
            else:
                max_so_far += num
                global_max = max(max_so_far, global_max)
        return global_max





print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#print Solution().maxSubArray([1, 2])