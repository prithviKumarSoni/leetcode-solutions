"""
Problem: Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/
Pattern: Binary Search (Lower Bound)
Key Idea:
- Find the first index where nums[index] >= target
- If target exists, return its index
- Otherwise, return the position where it should be inserted
Time: O(log n)
Space: O(1)
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lower = 0
        upper = n-1
        lb = 0
        if target > nums[upper]:
            return upper + 1
        # elif target < nums[lower]:
        #     return lower
        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] >= target:
                lb = mid
                upper = mid - 1
            else:
                lower = mid + 1
        
        
        return lb