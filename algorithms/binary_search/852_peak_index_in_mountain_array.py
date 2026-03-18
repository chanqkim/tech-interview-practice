"""
link: https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1951834322/?envType=problem-list-v2&envId=dsa-sorting-plateau-binary-search
"""

from typing import List


# time: O(log n) space: O(1)
# time analysis: binary search on the mountain array takes O(log n) time
# space analysis: using only a constant amount of extra space → O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # initialize pointers for binary search
        left, right = 0, len(arr) - 1

        # perform binary search to find the peak index
        while left < right:
            mid = left + (right - left) // 2

            # if the middle element is less than the next element, we are in the ascending part of the mountain
            if arr[mid] < arr[mid + 1]:
                left = mid + 1  # move right to search for the peak
            else:
                right = mid  # move left to search for the peak

        return left
