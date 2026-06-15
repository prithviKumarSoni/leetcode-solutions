"""
Problem: Majority Element
Pattern: Hashing / Frequency Counting
Key Idea: Count occurrences of each number using a hashmap. As soon as a count exceeds n//2, return that element.
Time: O(n)
Space: O(n)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > n//2:
                return num
        return -1