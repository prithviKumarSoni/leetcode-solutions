"""
Problem: Rearrange Array Elements by Sign
Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
Pattern: Two Pointers / Index Placement
Key Idea:
- Maintain separate indices for positive and negative positions
- Place positive numbers at even indices
- Place negative numbers at odd indices
Time: O(n)
Space: O(n)
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        pos = 0
        neg = 1
        for i in range(0,n):
            if nums[i] >= 0:
                result[pos] = nums[i]
                pos += 2
            else:
                result[neg] = nums[i]
                neg += 2
        
        return result