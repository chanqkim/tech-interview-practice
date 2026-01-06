"""
link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

Time: O(n)
Space: O(n)
Pattern: Queue + Simulation + Cycle Detection

Key Insight:
"If a full rotation happens without any state change, stop."
"""

from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Number of attempts allowed in one full rotation
        # If no student eats a sandwich during these attempts,
        # it means the process is stuck and should stop
        attempts = len(students)

        # Continue while there are students left
        # and at least one successful match is still possible
        while students and attempts > 0:
            # Case 1: Front student takes the top sandwich
            if students[0] == sandwiches[0]:
                # Remove both student and sandwich from the front
                students.pop(0)
                sandwiches.pop(0)

                # Reset attempts since a successful state change occurred
                attempts = len(students)

            # Case 2: Front student cannot take the sandwich
            else:
                # Move the front student to the back of the queue
                first_student = students.pop(0)
                students.append(first_student)

                # One failed attempt to prevent infinite loop
                attempts -= 1

        # Remaining students are unable to eat
        return len(students)
