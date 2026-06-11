"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Pattern: Hashing
Key Idea:
- Store seen elements in a hash map
- If an element is encountered again, a duplicate exists
- Otherwise add it to the hash map
Time: O(n)
Space: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            hash_map[num] = True
        return False