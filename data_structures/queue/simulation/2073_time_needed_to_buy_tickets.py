"""
link: https://leetcode.com/problems/time-needed-to-buy-tickets/description/?envType=problem-list-v2&envId=dsa-sequence-valley-queue
"""

from collections import deque
from typing import List


# Time Complexity: O(sum(tickets))
#   - Each ticket purchase takes 1 second
#   - Total operations equal the total number of tickets sold
# Space Complexity: O(n)
#   - Queue stores up to n people
class Solution1:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Initialize a queue to simulate the line
        # Each element is a tuple: (original_index, remaining_tickets)
        queue = deque()
        for i in range(len(tickets)):
            queue.append((i, tickets[i]))  # Store index to identify person k later

        # This variable tracks the total elapsed time (seconds)
        answer = 0

        # Continue simulation while there are people in the queue
        while queue:
            # Take the person at the front of the queue
            index, remaining_tickets = queue.popleft()

            # The person buys exactly one ticket (1 second passes)
            remaining_tickets -= 1
            answer += 1

            # If this person is k and they just bought their last ticket,
            # we stop the simulation immediately
            if remaining_tickets == 0 and index == k:
                break

            # If the person still needs more tickets,
            # they go back to the end of the queue
            if remaining_tickets > 0:
                queue.append((index, remaining_tickets))

        # Return the total time until person k finishes buying tickets
        return answer


# Counting Approach
# Time Complexity: O(n)
#   - Single pass through the tickets list
# Space Complexity: O(1)
class Solution2:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        target = tickets[k]

        for i in range(len(tickets)):
            if i <= k:
                # People before or at k can buy up to `target` tickets
                time += min(tickets[i], target)
            else:
                # People after k cannot buy on k's last turn
                time += min(tickets[i], target - 1)

        return time
