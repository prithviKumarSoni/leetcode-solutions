"""
Problem: Maximum Sum of Distinct Subarrays With Length K
Link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
Pattern: Sliding Window + Hash Map
Key Idea:
- Maintain a fixed-size sliding window of length k
- Use frequency map to track distinct elements
- Update maximum sum only when all elements in window are unique
Time: O(n)
Space: O(k)
"""

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        curr_sum = 0
        max_sum = 0
        left = 0
        for right in range(len(nums)):
            
            curr_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if right - left + 1 > k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                
                curr_sum -= nums[left]
                left += 1

            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, curr_sum)
        
        return max_sum