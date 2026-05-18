'''
link: https://leetcode.com/problems/decode-string/description/?envType=problem-list-v2&envId=dsa-recursion-maze-recursion
'''

# using a stack to decode the string iteratively
# time analysis: O(n × k) where n is the length of the input string and k is the maximum repeat count, because in the worst case we may have to repeat a substring of length m up to k times, leading to O(m × k) for that part, and if this happens for multiple parts of the string, it can lead to O(n × k) overall
# space analysis: O(n) in the worst case if we have nested structures that require storing multiple levels of strings and repeat counts on the stack, especially if the input string is large and has many nested brackets
class Solution:
    def decodeString(self, s: str) -> str:  # ← self 추가

        # initialize a stack to keep track of previous strings and repeat counts, and variables for the current string and number
        stack = []
        current_str = ""
        current_num = 0

        # loop through each character in the input string
        for char in s:
            
            # if the character is a digit, build the current number (repeat count) by multiplying the existing number by 10 and adding the new digit
            if char.isdigit():
                
                current_num = current_num * 10 + int(char)

            # if the character is an opening bracket '[', push the current string and number onto the stack, and reset them for the new context inside the brackets
            elif char == '[':
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0

            # if the character is a closing bracket ']', pop the previous string and number from the stack, and combine it with the current string repeated by the number
            elif char == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num

            else:
                # if the character is a letter, add it to the current string
                current_str += char

        return current_str