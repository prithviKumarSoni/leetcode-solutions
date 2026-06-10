"""
Problem: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Pattern: Hash Map + Frequency Counting
Key Idea:
- Count frequency of each element using Counter
- Retrieve the k most frequent elements using most_common(k)
Time: O(n log k)  (implementation dependent)
Space: O(n)
"""
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency_counter = Counter(nums)
        most_common_elements = frequency_counter.most_common(k)
        result = [element for element, count in most_common_elements]
        return result