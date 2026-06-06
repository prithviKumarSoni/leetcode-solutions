"""
Problem: Search in Rotated Sorted Array II
Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
Pattern: Modified Binary Search
Key Idea:
- One half is usually sorted, similar to Rotated Sorted Array I
- Duplicates can make it impossible to identify the sorted half
- When nums[low] == nums[mid] == nums[high], shrink the search space
- Otherwise, determine the sorted half and continue binary search
Time: O(log n) average, O(n) worst case
Space: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0 
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid]==target:
                return True
            
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
        return False 