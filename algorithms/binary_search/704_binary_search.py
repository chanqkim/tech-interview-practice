"""
link: https://leetcode.com/problems/binary-search/description/?envType=problem-list-v2&envId=dsa-sorting-plateau-binary-search
"""

from typing import List


# time: O(log n) space: O(1)
# time analysis: binary search on the sorted array takes O(log n) time
# space analysis: using only a constant amount of extra space → O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize pointers for binary search
        left, right = 0, len(nums) - 1

        # perform binary search to find the target index
        while left <= right:
            # calculate the middle index
            mid = (left + right) // 2

            # check if the middle element is the target
            if nums[mid] == target:
                return mid
            # if the middle element is less than the target, search in the right half
            elif nums[mid] < target:
                left = mid + 1
            # if the middle element is greater than the target, search in the left half
            else:
                right = mid - 1
        # if the target is not found in the array, return -1
        return -1
