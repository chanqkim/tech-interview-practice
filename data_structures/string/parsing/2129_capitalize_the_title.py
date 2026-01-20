"""
link: https://leetcode.com/problems/masking-personal-information/?envType=problem-list-v2&envId=dsa-sequence-valley-string

String utility methods used:
- isdigit()  : checks if a character is a numeric digit (0–9)
- isalpha()  : checks if a character is an alphabet letter
- isalnum()  : checks if a character is alphanumeric (letter or digit)
- islower()  : checks if a character is lowercase
- isupper()  : checks if a character is uppercase
"""


# Time Complexity: O(n)
# - We iterate through the string at most once
# Space Complexity: O(n)
# - Temporary storage for extracted digits or rebuilt strings
class Solution:
    def maskPII(self, s: str) -> str:
        # Case 1: Email address
        if "@" in s:
            s = s.lower()
            name, domain = s.split("@")

            # Keep first and last character, mask the middle
            masked_name = name[0] + "*****" + name[-1]

            return masked_name + "@" + domain

        # Case 2: Phone number
        else:
            # Extract digits only using isdigit()
            digits = [c for c in s if c.isdigit()]
            total_len = len(digits)

            # Last 4 digits are always visible
            local = "***-***-" + "".join(digits[-4:])

            # If no country code
            if total_len == 10:
                return local

            # With country code
            country_len = total_len - 10
            country = "+" + "*" * country_len + "-"

            return country + local
