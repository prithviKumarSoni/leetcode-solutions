"""
Problem: Contains Duplicate II
Pattern: Hashing
Key Idea: Store the most recent index of each value. If the same value is seen again and the index difference is at most k, return True.
Time: O(n)
Space: O(n)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for current_index, value in enumerate(nums):
            if value in index_map and current_index - index_map[value] <= k:
                return True
            index_map[value] = current_index
        return False