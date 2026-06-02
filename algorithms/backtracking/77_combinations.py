'''
link: https://leetcode.com/problems/combinations/description/?envType=problem-list-v2&envId=dsa-recursion-maze-backtracking
'''

# time analysis: O(k × C(n, k)) where C(n, k) is the number of combinations of n items taken k at a time, because we generate C(n, k) combinations and each combination takes O(k) time to construct
# space analysis: O(k) for the recursion stack and the path list
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        # define a backtracking function that takes the starting number as an argument, and recursively builds combinations by adding numbers to the path until the path length equals k, at which point it adds a copy of the path to the result list
        def backtrack(start):
            
            # if the current path has reached the desired length k, add a copy of it to the result list and return to explore other combinations
            if len(path) == k:
                result.append(path[:])
                return

            # loop through numbers starting from the given start number up to n
            for num in range(start, n + 1):
                
                # add the current number to the path 
                path.append(num)
                # recursively call backtrack with the next number to continue building the combination
                backtrack(num + 1)

                # backtrack by removing the last number added to the path, allowing the function to explore other combinations with different numbers
                path.pop()

        backtrack(1)

        return result