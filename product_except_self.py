from operator import mul

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0]*len(nums)
        elif zero_count == 1:
            idx = nums.index(0)
            ans = [0]*len(nums)
            ans[idx] = reduce(mul, nums[0:idx]+nums[idx+1:], 1)
            return ans
        else:
            prod = reduce(mul, nums, 1)
            return [prod/nums[idx] for idx in xrange(len(nums))]
