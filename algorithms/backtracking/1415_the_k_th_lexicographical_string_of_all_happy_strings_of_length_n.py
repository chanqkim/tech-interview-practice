'''
link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/?envType=problem-list-v2&envId=dsa-recursion-maze-backtracking
'''

# time:  O(n · 2^n)
# space: O(n)
# time analysis: O(n · 2^n) because we are generating all possible happy strings of length n, and there are 3 choices for the first character, 2 choices for each subsequent character (since it cannot be the same as the previous one), leading to a total of 3 * 2^(n-1) = O(n · 2^n) in the worst case when n is large
# space analysis: O(n) for the recursion stack and the path list, since the maximum depth of the recursion is n 
class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        result = []
        path = []

        # function to generate all happy strings of length n using backtracking, where we build the string character by character, ensuring that no two adjacent characters are the same, and add valid strings to the result list until we have generated all possible combinations
        def backtrack():
            
            # if the current path has reached the desired length n
            if len(path) == n:
                # add the joined string to the result list and return to explore other combinations
                result.append("".join(path))
                return

            # loop through the characters 'a', 'b', and 'c' to build the happy string
            for ch in "abc":
                
                # if the current character is the same as the last character in the path, skip it to ensure that no two adjacent characters are the same
                if path and path[-1] == ch:
                    continue

                # add the current character to the path and recursively call backtrack to continue building the string
                path.append(ch)

                backtrack()

                # backtrack by removing the last character added to the path, allowing the function to explore other combinations with different characters
                path.pop()

        # start the backtracking process to generate all happy strings of length n
        backtrack()

        # return the k-th happy string from the result list if k is within the bounds of the list, otherwise return an empty string
        return result[k - 1] if k <= len(result) else ""