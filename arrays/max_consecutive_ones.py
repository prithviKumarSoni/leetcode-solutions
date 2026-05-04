"""
Problem: Max Consecutive Ones
Link: https://leetcode.com/problems/max-consecutive-ones/
Pattern: Array Traversal (Counting Streak)
Key Idea:
- Count consecutive 1s
- Reset count when 0 is encountered
- Track maximum streak using max_length
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_length = 0
        
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_length = max(max_length, count)
                count = 0

        return max(max_length, count)