"""
Problem: Subarray Sum Equals K
Pattern: Prefix Sum + Hashing
Key Idea: If current_prefix_sum - previous_prefix_sum = k, then the subarray between them has sum k. Store frequencies of prefix sums in a hashmap and count how many times (current_sum - k) has appeared.
Time: O(n)
Space: O(n)
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = Counter({0: 1})
      
        result = 0
        current_sum = 0
      
        for num in nums:
            current_sum += num
    
            result += prefix_sum_count[current_sum - k]
          
            prefix_sum_count[current_sum] += 1
      
        return result