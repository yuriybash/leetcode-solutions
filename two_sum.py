"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.
"""

import collections

class Solution(object):
    def twoSum(self, nums, target):

        mapped = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            mapped[num].append(idx)

        for idx, num in enumerate(nums):
            if (target-num) in mapped:
                matching_indices = mapped[target-num]
                for match in matching_indices:
                    if match != idx:
                        return sorted([idx, match])

        return []
