'''
link: https://leetcode.com/problems/3sum-closest/submissions/1965855705/?envType=problem-list-v2&envId=dsa-recursion-maze-two-pointers
'''

from typing import List

# time: O(n^2) space: O(1)
# time analysis: sorting takes O(n log n), and the two-pointer approach takes O(n^2) in the worst case, leading to an overall time complexity of O(n^2)
# space analysis: using only a constant amount of extra space for the two pointers and a variable to store the closest sum → O(1)
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # sort input array
        nums.sort()
        # initialize closest sum with a large value
        closest = float('inf')
        
        # loop through the sorted array and use two pointers to find the closest sum of three numbers
        for i in range(len(nums) - 2):
            # initialize two pointers: left starts at the next element after i, and right starts at the end of the array
            left, right = i + 1, len(nums) - 1

            # loop until the two pointers meet
            while left < right:
                # calculate the sum of the three numbers at indices i, left, and right
                total = nums[i] + nums[left] + nums[right]

                # if total value is closer to the target than the current closest value, update closest
                if abs(total - target) < abs(closest - target):
                    closest = total
                
                # if total value is equal to the target, return total 
                if total == target:
                    return total
                # if total value is smaller, move smaller value pointer(left) to the right to increase the total value
                elif total < target:
                    left += 1
                # if total value is larger, move larger value pointer(right) to the left to decrease the total value
                else:
                    right -= 1

        return closest