"""
Problem: Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/
Pattern: Two Pointers
Key Idea:
- Find first zero position (i)
- Use another pointer (j) to scan ahead
- When non-zero is found, swap with nums[i] and move i forward
Time: O(n)
Space: O(1)
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
        if i == len(nums):
            return

        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
