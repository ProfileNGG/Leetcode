class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        reversed_number = 0
        number = x
        while x > 0:
            digit = x % 10
            x = x // 10
            reversed_number = reversed_number * 10 + digit

        return number == reversed_number
        