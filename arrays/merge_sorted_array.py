
"""
Problem: Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/
Pattern: Two Pointers (from end)
Key Idea:
- Use three pointers (i, j, k)
- Compare elements from the end of both arrays
- Fill nums1 from the back to avoid overwriting
Time: O(m + n)
Space: O(1)
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n -1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        


