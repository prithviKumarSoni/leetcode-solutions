"""
Problem: Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/
Pattern: Kadane's Algorithm
Key Idea:
- Maintain running subarray sum
- If running sum becomes negative, reset it to 0
- Track maximum sum seen so far
Time: O(n)
Space: O(1)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        total = 0
        for i in nums:
            total = total + i
            maxi = max(maxi, total)
            if total < 0:
                total = 0
        return maxi