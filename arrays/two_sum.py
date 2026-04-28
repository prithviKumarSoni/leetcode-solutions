"""
Problem: Two Sum
Pattern: HashMap (store seen numbers)
Key Idea: For each number, check if (target - num) already exists
Time: O(n)
Space: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hash_map = {}
        for i in range(0,n):
            j = target - nums[i]
            
            if j in hash_map:
                return [hash_map[j], i]
            hash_map[nums[i]] = i
            