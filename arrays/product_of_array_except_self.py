"""
Problem: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/
Pattern: Prefix Product + Suffix Product
Key Idea:
- Store prefix product in answer array
- Traverse from right to maintain suffix product
- Multiply prefix and suffix products for final result
Time: O(n)
Space: O(1) excluding output array
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n

        prefix = 1

        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        sufix = 1

        for i in range(n -1, -1, -1):
            ans[i] *= sufix
            sufix *= nums[i]
        
        return ans