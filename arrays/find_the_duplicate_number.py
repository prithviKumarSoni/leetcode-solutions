"""
Problem: Find the Duplicate Number
Pattern: Hashing (Set)
Key Idea: Store visited numbers in a set. If a number is encountered again, it is the duplicate.
Time: O(n)
Space: O(n)
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = set()
        for num in nums:
            if num in freq:
                return num
            freq.add(num)
        
        return -1