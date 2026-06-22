"""
Problem: Running Sum of 1d Array
Pattern: Prefix Sum
Key Idea: Maintain a running prefix sum and append it to the result array at each step.
Time: O(n)
Space: O(n)
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        presum = 0
        new_nums = []
        n = len(nums)
        for num in nums:
            presum += num
            new_nums.append(presum)
        return new_nums

