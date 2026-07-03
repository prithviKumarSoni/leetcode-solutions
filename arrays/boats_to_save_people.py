"""
Problem: Boats to Save People
Pattern: Two Pointers + Greedy
Key Idea: Sort the array and pair the lightest person with the heaviest whenever possible. Otherwise, send the heaviest person alone.
Time: O(n log n)
Space: O(1)
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
    
        left = 0                    
        right = len(people) - 1       
        boats = 0
        
        
        while left <= right:
            
            if people[left] + people[right] <= limit:
                left += 1             
            
            right -= 1                
            boats += 1                
            
        return boats
