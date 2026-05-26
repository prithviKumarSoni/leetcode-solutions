"""
Problem: Minimum Size Subarray Sum
Link: https://leetcode.com/problems/minimum-size-subarray-sum/
Pattern: Variable Size Sliding Window
Key Idea:
- Expand window until sum >= target
- Shrink window from left to minimize length
- Track smallest valid window size
Time: O(n)
Space: O(1)
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):

        min_len = float("inf")
        left = 0
        currsum = 0

        for right in range(len(nums)):
            currsum += nums[right]

            while currsum >= target:
                min_len = min(min_len, right - left + 1)

                currsum -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len