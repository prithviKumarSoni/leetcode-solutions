"""
Problem: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Pattern: Sliding Window
Key Idea:
- Maintain a window with unique characters using a set
- Expand window using right pointer
- Shrink window from left when duplicate character appears
- Track maximum window size
Time: O(n)
Space: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        max_count = 0
        left = 0
        for right in range(len(s)):
            
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            
            my_set.add(s[right])
            cur_window = right - left +1
            max_count = max(max_count, cur_window)
        return max_count