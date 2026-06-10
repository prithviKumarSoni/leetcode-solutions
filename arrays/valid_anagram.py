"""
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Pattern: Hash Map / Frequency Counting
Key Idea:
- Count frequency of each character in both strings
- Compare character frequencies
- If all frequencies match, strings are anagrams
Time: O(n)
Space: O(k)

where:
n = length of string
k = number of unique characters
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        for key in dict_s:
            if dict_s[key] != dict_t.get(key, 0):
                return False
            
        return True