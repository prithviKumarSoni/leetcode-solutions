"""
Problem: Rotate Array
Link: https://leetcode.com/problems/rotate-array/
Pattern: Array Slicing
Key Idea:
- Normalize k using k % n
- Take last k elements and move them to front
- Append remaining elements after that
Time: O(n)
Space: O(n)
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]