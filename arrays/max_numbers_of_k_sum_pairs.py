"""
Problem: Max Number of K-Sum Pairs
Pattern: Sorting + Two Pointers
Key Idea: Sort the array and use two pointers to pair the smallest and largest values. Move pointers based on whether the current sum is less than, equal to, or greater than k.
Time: O(n log n)
Space: O(1)
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = (len(nums) - 1)

        operation_count = 0

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                operation_count += 1
                left += 1
                right -= 1
            elif current_sum > k:
                right -= 1
            else:
                left += 1
        return operation_count