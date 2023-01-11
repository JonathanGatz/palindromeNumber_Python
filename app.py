class Solution(object):
    def isPalindrome(self, x):

        return False if x < 0 else x == int(str(x)[::-1])

# Palindrome cannot be a negative number
# Attach the string to the intigers and use [::-1] to reverse


