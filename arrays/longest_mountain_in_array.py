"""
Problem: Longest Mountain in Array
Pattern: Dynamic Programming (Prefix & Suffix Arrays)
Key Idea: Compute the increasing length ending at each index and the decreasing length starting at each index. A valid mountain has both lengths greater than 1, and its length is left[i] + right[i] - 1.
Time: O(n)
Space: O(n)
"""

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
      
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                left[i] = left[i - 1] + 1
      
        max_length = 0

        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                right[i] = right[i + 1] + 1
              
                if left[i] > 1:
                    max_length = max(max_length, left[i] + right[i] - 1)
      
        return max_length