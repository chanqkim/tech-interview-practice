'''
link: https://leetcode.com/problems/reverse-pairs/?envType=problem-list-v2&envId=dsa-sorting-plateau-divide-and-conquer
'''

from typings import List

# Time Complexity: O(n log n)
# - Standard merge sort complexity
# - Each level does O(n) work (merge + counting)
# - Total levels = log n
# Space Complexity: O(n)
# - Temporary arrays created during merge
# - Recursive call stack = O(log n), but overall dominated by O(n) auxiliary space
class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge_sort(arr):
            # Base case: single element → no reverse pairs
            if len(arr) <= 1:
                return arr, 0

            # Split array into two halves
            mid = len(arr) // 2

            # Recursively sort left half and count pairs inside it
            left, left_count = merge_sort(arr[:mid])

            # Recursively sort right half and count pairs inside it
            right, right_count = merge_sort(arr[mid:])

            # Initialize count with pairs found in subproblems
            count = left_count + right_count

            # Count cross reverse pairs (left[i] > 2 * right[j])
            j = 0
            for i in range(len(left)):
                # Move pointer j while condition holds
                # Since both halves are sorted, j only moves forward → O(n)
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                # All elements in right[0...j-1] satisfy condition for current left[i]
                count += j

            # Merge step (standard merge sort merge)
            merged = []

            # Reset pointers for merging
            i = j = 0

            # Merge two sorted arrays
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])  # take from left
                    i += 1
                else:
                    merged.append(right[j])  # take from right
                    j += 1

            # Append remaining elements (only one side will have leftovers)
            merged.extend(left[i:])
            merged.extend(right[j:])

            # Return sorted array + total reverse pair count
            return merged, count

        # only return the count value
        return merge_sort(nums)[1]