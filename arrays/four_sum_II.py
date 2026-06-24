"""
Problem: 4Sum II
Pattern: Hashing + Pair Sums
Key Idea: Store frequencies of all pair sums from nums1 and nums2. For each pair sum from nums3 and nums4, look for its negation in the hashmap.
Time: O(n²)
Space: O(n²)
"""

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        sum_count = Counter(a + b for a in nums1 for b in nums2)
        result = sum(sum_count[-(c + d)] for c in nums3 for d in nums4)
        return result