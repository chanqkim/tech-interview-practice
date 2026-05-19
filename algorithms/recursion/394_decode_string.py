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

# using recursion to decode the string
# time analysis: O(n × k) where n is the length of the input string and k is the maximum repeat count, because in the worst case we may have to repeat a substring of length m up to k times, leading to O(m × k) for that part, and if this happens for multiple parts of the string, it can lead to O(n × k) overall
# space analysis: O(n) in the worst case if we have nested structures that require storing multiple levels of strings and repeat counts on the stack, especially if the input string is large and has many nested brackets
class Solution2:
    def decodeString(self, s: str) -> str:

        # initialize an index variable as a list to allow modification inside the nested decode function (since integers are immutable in Python)
        idx = [0]

        def decode() -> str:
            # set variables for the current number (repeat count) and the current result string
            result = ""  

            # loop until we reach the end of the string, processing characters one by one
            while idx[0] < len(s):  
                # read the character at the current index
                char = s[idx[0]]    
                
                # if the character is a digit, parse the full number (which may have multiple digits) to get the repeat count for the upcoming bracketed string
                if char.isdigit():
                    # reset num to 0 before parsing a new number, then loop through the digits to build the full number (e.g. "12" becomes 12)
                    num = 0  
                    # parse the number by looping through consecutive digits and building the integer value (e.g. "12[a]")
                    while s[idx[0]].isdigit():           
                        # Shift left and add current digit (e.g. 1 → 10 → 12)
                        num = num * 10 + int(s[idx[0]])  
                        # move the index to the next character to continue parsing the number
                        idx[0] += 1     
                    # After parsing the number, the index is now at the character immediately following the digits, which should be the opening bracket '[' that indicates the start of the substring to repeat. We will handle this in the next part of the loop.                 
                    continue  

                # if the character is an opening bracket '[', recursively decode the substring inside the brackets and then repeat it according to the previously paresed number
                # The recursive call will handle everything until it finds the corresponding closing bracket ']'.
                elif char == '[':
                    # decode() will return the decoded string inside the brackets, and we will repeat it num times and append to the result
                    idx[0] += 1       
                    inner = decode()  
                    # decode() will return the decoded string inside the brackets, and we will repeat it num times and append to the result
                    result += inner * num  
                # if the character is a closing bracket ']', this means finished decoding the current bracketed substring
                elif char == ']':
                    # move the index past the closing bracket ']' to prepare for returning to the caller
                    idx[0] += 1
                    # return the result of the current bracketed substring to the caller 
                    return result  
                
                # if the character is a regular letter (a-z), append it directly to the result and move the index to the next character
                else:
                    result += char  
                    idx[0] += 1     
            
            # after exiting the loop, return the decoded string 
            return result 
        
        # call the decode function to start decoding
        return decode()  

