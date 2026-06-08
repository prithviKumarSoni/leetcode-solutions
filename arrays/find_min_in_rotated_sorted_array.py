"""
Problem: Find Minimum in Rotated Sorted Array
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Pattern: Modified Binary Search
Key Idea:
- In a rotated sorted array, one half is always sorted
- If right half is sorted, the minimum may be at mid or to its left
- If left half is sorted, its first element is a candidate minimum
- Discard the sorted half and continue searching in the unsorted half
Time: O(log n)
Space: O(1)
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        mini = float("inf")
        while low <= high:
            mid = (low+high)//2
            if nums[mid] < nums[high]:
                mini = min(mini, nums[mid])
                high = mid - 1
            else:
                mini = min(mini, nums[low])
                low = mid + 1
        return mini