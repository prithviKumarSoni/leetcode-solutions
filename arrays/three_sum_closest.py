"""
Problem: 3Sum Closest
Pattern: Sorting + Two Pointers
Key Idea: Sort the array, fix one element, and use two pointers to find the triplet whose sum is closest to the target.
Time: O(n²)
Space: O(1)
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closest_sum = float("inf")

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[right] + nums[left]

                if current_sum == target:
                    return current_sum

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum > target:
                    right -= 1

                else:
                    left += 1
        
        return closest_sum