"""
Given a sorted array, two integers k and x, find the k closest elements to x 
in the array. The result should also be sorted in ascending order. If there 
is a tie, the smaller elements are always preferred.
"""

import collections

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        Find the k closest elements in arr to k

        :param arr: the list
        :type: list
        :param k: the number of elements to get
        :type: int
        :param x: the target
        :type: int
        :return: an array with the closest elements
        :rtype: list
        """
        dist_to_elem = self.get_distance_distribution(arr, x)

        solution = sorted(self.get_k_elements(dist_to_elem, k))
        return solution

    @staticmethod
    def get_distance_distribution(input, target):
        """
        For each elem in input, calculate its distance (abs. difference) from
        the target, return a map of {distance: [elems]}

        :param input: the input list
        :type: list
        :param target: the target value
        :type target: int
        :return: a dict mapping distances to corresponding elements
        :rtype: collections.defaultdict
        """
        dist_to_elem = collections.defaultdict(list)

        for elem in input:
            dist = abs(elem - target)
            dist_to_elem[dist].append(elem)

        return dist_to_elem

    @staticmethod
    def get_k_elements(dist_to_elem, k):
        """
        Given a dict of the format {<dist.>: [elements with dist.]}, return
        the k closest elements (choose smaller in case of ties).

        :param dist_to_elem: map of distance to corresponding elements
        :type: collections.defaultdict
        :param k: number of elements to get
        :type k: int
        :return: list of k closest elements
        :rtype: list
        """

        k_elems = []

        for dist in sorted(dist_to_elem.keys()):
            for elem in sorted(dist_to_elem[dist]):
                k_elems.append(elem)
                if len(k_elems) == k:
                    return k_elems
