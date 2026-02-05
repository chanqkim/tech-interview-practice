"""
link: https://leetcode.com/problems/find-the-highest-altitude/?envType=problem-list-v2&envId=dsa-association-slope-prefix-sum
"""

from typing import List


# time: O(n) space: O(1)
# time analysis: traversing the entire list once → O(n)
# space analysis: using only a constant amount of extra space → O(1)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # initialize altitude and max altitude
        altitude = 0
        max_altitude = 0

        # calculate altitude at each point and update max altitude
        for i in gain:
            altitude += i
            # update max altitude if current altitude is higher
            max_altitude = max(max_altitude, altitude)
        return max_altitude
