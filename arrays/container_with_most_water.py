"""
Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/
Pattern: Two Pointers
Key Idea:
- Start with widest container using two pointers
- Area depends on minimum height and width
- Move pointer with smaller height to try finding a taller boundary
Time: O(n)
Space: O(1)
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            min_height = min(height[left], height[right])
            area = min_height*(right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area 
