"""
link: https://leetcode.com/problems/minimum-absolute-difference/?envType=problem-list-v2&envId=dsa-sorting-plateau-sorting
"""

from typing import List

# time: O(n log n) space: O(1)
# time analysis: sorting the array takes O(n log n), and a single pass to find
# the minimum absolute difference takes O(n), resulting in an overall time complexity of O(n log n).


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort array in ascending order
        arr.sort()

        # initialize minimum difference and result list
        min_diff = float("inf")
        result = []

        # loop through sorted array to find minimum absolute difference
        for i in range(1, len(arr)):
            # calculate the difference between adjacent elements
            diff = arr[i] - arr[i - 1]

            # update minimum difference and result list based on the calculated difference
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i - 1], arr[i]]]
            # if the calculated difference is equal to the current minimum difference, add the pair to the result list
            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result
