"""
Problem: Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Pattern: Two Pointers
Key Idea:
- Largest square comes from element with largest absolute value
- Compare leftmost and rightmost elements
- Fill result array from the end
Time: O(n)
Space: O(n)
"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [0] * n
        
        left = 0
        right = n-1
        for i in range(n-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                answer[i] = nums[left] ** 2
                left += 1
            else: 
                answer[i] = nums[right] ** 2
                right -= 1
        
        return answer

