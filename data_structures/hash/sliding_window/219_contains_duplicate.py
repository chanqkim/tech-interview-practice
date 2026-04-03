'''
link: https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=dsa-recursion-maze-sliding-window
'''

from typing import List

# time: O(n) space: O(k)
# time analysis: each element is added and removed from the set at most once → O(n
# space analysis: the set contains at most k elements at any time → O(k)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Use a set to maintain a sliding window of the last k elements
        window = set()
        
        # loop through the array and check for duplicates in the current window
        for i, num in enumerate(nums):
            # Check if the current number is already in the window (duplicate found)
            if num in window:
                return True

            # if current number is not in the window, add it to the window
            window.add(num)

            # if the window size exceeds k, remove the oldest element (nums[i - k]) from the window
            if len(window) > k:
                window.remove(nums[i - k])
        # if we finish iterating through the array without finding duplicates within k distance, return False
        return False
