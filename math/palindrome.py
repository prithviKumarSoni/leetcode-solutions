"""
Problem: Palindrome Number
Pattern: Math (reverse digits)
Key Idea: Reverse number and compare with original
Time: O(log n)
Space: O(1)
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        reverse = 0
        while num > 0 :
            ld = num % 10
            reverse = reverse * 10 + ld
            num = num // 10

        return x == reverse