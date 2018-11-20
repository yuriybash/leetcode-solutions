from collections import OrderedDict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        frequency_to_nums = OrderedDict()
        num_to_frequency = {}

        for num in nums:
            if num in num_to_frequency:
                original_frequency = num_to_frequency[num]
                new_frequency = original_frequency + 1
                if new_frequency in frequency_to_nums:
                    frequency_to_nums[new_frequency].append(num)
                else:
                    frequency_to_nums[new_frequency] = [num]

                frequency_to_nums[original_frequency].remove(num)
                num_to_frequency[num]+=1

            else:
                num_to_frequency[num] = 1
                if 1 in frequency_to_nums:
                    frequency_to_nums[1].append(num)
                else:
                    frequency_to_nums[1] = [num]

        top_k = []
        for freq_count in reversed(frequency_to_nums.keys()):
            for num in frequency_to_nums[freq_count]:
                top_k.append(num)

                if len(top_k) == k:
                    return top_k
        return top_k
