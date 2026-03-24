'''
link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=dsa-sorting-plateau-binary-search
'''

from typing import List

# time: O(log n) space: O(1)
# time analysis: binary search on the rotated sorted array takes O(log n) time
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

            # determine which half of the array is sorted
            if nums[left] <= nums[mid]:  
                # if target is in the left half, move the right pointer to mid - 1
                if nums[left] <= target < nums[mid]:  
                    right = mid - 1
                # if target is in the right half, move the left pointer to mid + 1
                else:  
                    left = mid + 1
            # right half is sorted
            else:  
                # target is in the right half, move the left pointer to mid + 1
                if nums[mid] < target <= nums[right]:  
                    left = mid + 1
                # target is in the left half
                else:  
                    right = mid - 1

        # if the target is not found in the array, return -1
        return -1