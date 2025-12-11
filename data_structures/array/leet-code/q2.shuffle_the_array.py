"""
link: https://leetcode.com/problems/shuffle-the-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
"""

from typing import List


# solution1: O(n) space: O(n)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:n]
        nums2 = nums[n:]
        answer = []
        for i in range(len(nums1)):
            answer.append(nums1[i])
            answer.append(nums2[i])
        return answer


# solution2: single loop, using index
class Solution2:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i in range(n):
            answer.append(nums[i])
            answer.append(nums[i + n])
        return answer


# solution3: using zip function
class Solution3:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for x, y in zip(nums[:n], nums[n:]):
            answer.extend([x, y])
        return answer
