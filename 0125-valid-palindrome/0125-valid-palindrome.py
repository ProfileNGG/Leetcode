import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        formatted = re.sub(r'[^A-Za-z0-9]+', '', s).lower()

        # Set up left and right pointers for palindrome check
        left, right = 0, len(formatted) - 1

        # Check if the string is a palindrome
        while left <= right:
            if formatted[left] != formatted[right]:
                return False
            left += 1
            right -= 1

        # If the loop completes, the string is a palindrome
        return True