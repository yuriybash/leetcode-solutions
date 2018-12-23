class Solution(object):
    def permute(self, nums):

        all_permutations = []

        def inner(existing, remaining):
            if len(remaining) == 1:
                all_permutations.append(existing + remaining)
            else:
                for idx in range(len(remaining)):
                    inner(existing + [remaining[idx]], remaining[0:idx] + remaining[idx + 1:])

        inner([], nums)
        return all_permutations
