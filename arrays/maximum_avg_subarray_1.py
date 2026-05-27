"""
Problem: Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i/
Pattern: Fixed Size Sliding Window
Key Idea:
- Maintain a window of size k
- Track sum of current window
- Update maximum sum and slide window forward
Time: O(n)
Space: O(1)
"""

class Solution(object):
    def findMaxAverage(self, nums, k):

        curr_sum = 0
        max_sum = float("-inf")
        left = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)

                curr_sum -= nums[left]
                left += 1

        return float(max_sum) / k