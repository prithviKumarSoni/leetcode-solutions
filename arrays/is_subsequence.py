"""
Problem: Is Subsequence
Pattern: Two Pointers
Key Idea: Traverse both strings with two pointers. Move the pointer in the subsequence only when characters match. If all characters in the subsequence are matched in order, return True.
Time: O(n)
Space: O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)