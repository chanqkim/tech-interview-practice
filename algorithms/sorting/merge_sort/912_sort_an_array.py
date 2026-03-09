"""
link:  https://leetcode.com/problems/sort-an-array/submissions/1942919137/?envType=problem-list-v2&envId=dsa-sorting-plateau-counting-sort-merge-sort-quickselect

Key Idea:
Merge Sort Algorithm

1. divide
array → left / right

2. conquer
recursively sort left and right halves

3. merge
merge two sorted halves into one sorted array
"""

from typing import List


# time: O(n log n) space: O(n)
# time analysis: merge sort divides the array into halves log n times, and merging takes O(n) time, resulting in an overall time complexity of O(n log n).
# space analysis: merge sort requires O(n) space for the temporary arrays used during the merging process, resulting in an overall space complexity of O(n).
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # recursive merge sort function
        # takes an array and returns a new sorted array
        def merge_sort(arr):
            # base case: arrays of size 0 or 1 are already sorted
            if len(arr) <= 1:
                return arr

            # find the middle index to divide the array into two halves
            mid = len(arr) // 2

            # recursively sort the left half
            left = merge_sort(arr[:mid])

            # recursively sort the right half
            right = merge_sort(arr[mid:])

            # merge the two sorted halves into one sorted array
            return merge(left, right)

        # helper function that merges two sorted arrays
        # into one sorted array
        def merge(left, right):
            # result list that will contain the merged sorted elements
            result = []

            # pointers for traversing left and right arrays
            i = j = 0

            # compare elements from both arrays and append the smaller one
            # this maintains the sorted order
            while i < len(left) and j < len(right):
                # if the current element in left is smaller or equal
                if left[i] <= right[j]:
                    result.append(left[i])  # add it to result
                    i += 1  # move left pointer forward

                else:
                    result.append(right[j])  # otherwise append right element
                    j += 1  # move right pointer forward

            # if there are remaining elements in left array
            # append them directly (they are already sorted)
            result.extend(left[i:])

            # if there are remaining elements in right array
            result.extend(right[j:])

            # return the fully merged sorted array
            return result

        # start merge sort on the input array and return the sorted result
        return merge_sort(nums)
