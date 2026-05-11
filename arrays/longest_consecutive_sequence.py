"""
Problem: Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Pattern: Hash Set / Sequence Expansion
Key Idea:
- Store all numbers in a set for O(1) lookup
- Start counting only when current number is the beginning of a sequence
- Expand sequence using consecutive numbers
Time: O(n)
Space: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        for i in range(0, len(nums)):
            my_set.add(nums[i])

        longest = 0
        for num in my_set:
            if num-1 not in my_set:
                x = num
                count = 1
                while x+1 in my_set:
                    count += 1
                    x += 1
                longest = max(longest, count)
        return longest