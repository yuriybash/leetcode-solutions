class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        combos = []
        nums.sort()

        for idx in xrange(len(nums)-2):
            l = idx + 1
            r = len(nums)-1

            while l < r:

                s = nums[idx] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    combos.append((nums[idx], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return list(set(combos))





print Solution().threeSum([-1, 0, 1, 2, -1, -4])