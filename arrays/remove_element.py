"""
Problem: Remove Element
Link: https://leetcode.com/problems/remove-element/
Pattern: Two Pointers
Key Idea:
- Use one pointer to scan array
- Use another pointer to place valid elements
- Overwrite elements equal to val in-place
Time: O(n)
Space: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        for i in range(n):
            if nums[i] != val:
                nums[left] = nums[i]
                left +=1
        return left