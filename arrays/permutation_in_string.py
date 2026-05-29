"""
Problem: Permutation in String
Link: https://leetcode.com/problems/permutation-in-string/
Pattern: Fixed Size Sliding Window + Frequency Map
Key Idea:
- Maintain a window of size len(s1)
- Track character frequency difference using Counter
- If all needed character counts become 0, a permutation exists
Time: O(n)
Space: O(1)  # only lowercase English letters
"""

from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        char_count = Counter(s1)
        char_needed = len(char_count)
        window_size = len(s1)

        for index, char in enumerate(s2):
            char_count[char] -= 1

            if char_count[char] == 0:
                char_needed -= 1

            if index >= window_size:
                left_char = s2[index - window_size]

                if char_count[left_char] == 0:
                    char_needed += 1

                char_count[left_char] += 1

            if char_needed == 0:
                return True

        return False