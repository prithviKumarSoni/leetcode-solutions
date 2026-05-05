"""
Problem: Missing Number
Link: https://leetcode.com/problems/missing-number/
Pattern: Hashing (Frequency Map)
Key Idea:
- Initialize a map for numbers from 0 to n
- Mark numbers present in the array
- The number with value 0 is the missing one
Time: O(n)
Space: O(n)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}

        for i in range(0, n+1):
            freq[i] = 0

        for num in nums:
            freq[num] = 1
        
        for k,v in freq.items():
            if v==0:
                return k