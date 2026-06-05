"""
Problem: Search in Rotated Sorted Array
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Pattern: Modified Binary Search
Key Idea:
- At least one half is always sorted
- Identify the sorted half
- Check if target lies within that half
- Discard the other half and continue searching
Time: O(log n)
Space: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
