'''
link: https://leetcode.com/problems/beautiful-array/submissions/1958926570/?envType=problem-list-v2&envId=dsa-sorting-plateau-divide-and-conquer
'''
from typing import List

# time: O(n) space: O(n)
# time analysis: each iteration generates a new array of size at most n, and the number of iterations is O(log n) since the size of the array doubles each time → O(n)
# space analysis: the size of the array generated in each iteration is at most n, and we store only one array at a time → O(n)

class Solution:
    def beautifulArray(self, n: int):
        # initialize the result array with the first element 1
        result = [1]

        # loop until the size of the result array is n
        while len(result) < n:
            tmp = []

            # add odd part
            for x in result:
                if 2 * x - 1 <= n:
                    tmp.append(2 * x - 1)

            # add even part
            for x in result:
                if 2 * x <= n:
                    tmp.append(2 * x)

            result = tmp

        return result   