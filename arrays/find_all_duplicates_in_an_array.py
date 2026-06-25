"""
Problem: Find All Duplicates in an Array
Pattern: Hashing (Set)
Key Idea: Use a set to track seen numbers. If a number is encountered again, add it to the result.
Time: O(n)
Space: O(n)
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = []

        for num in nums:
            if num in seen:
                duplicate.append(num)
            seen.add(num)

        return duplicate