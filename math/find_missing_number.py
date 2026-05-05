"""
Problem: Missing Number
Pattern: Math (Sum Formula)
Key Idea:
- Sum of 0..n = n*(n+1)/2
- Subtract actual sum to find missing number
Time: O(n)
Space: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1)//2) - sum(nums)