"""
Problem: Single Number
Pattern: Hashing / Frequency Counting
Key Idea: Count occurrences of each number using a hashmap and return the number whose frequency is 1.
Time: O(n)
Space: O(n)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:
            if freq[num] == 1:
                return num