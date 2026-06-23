"""
Problem: Find All Numbers Disappeared in an Array
Pattern: Hashing
Key Idea: Store all existing numbers in a hash set/map, then iterate from 1 to n and collect numbers that are missing.
Time: O(n)
Space: O(n)
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash = {}
        lis = []
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        
        for i in range(1, len(nums)):
            if i not in hash:
                lis.append(i)
        return lis