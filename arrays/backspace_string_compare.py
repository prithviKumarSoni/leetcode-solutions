"""
Problem: Backspace String Compare
Pattern: Two Pointers (Reverse Traversal)
Key Idea: Traverse both strings from the end while tracking pending backspaces. Compare the next valid characters without constructing the final strings.
Time: O(n + m)
Space: O(1)
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
         # Initialize pointers at the end of both strings
        i = len(s) - 1
        j = len(t) - 1
        skip_s = 0  # Count of backspaces to skip in string s
        skip_t = 0  # Count of backspaces to skip in string t
      
       
        while i >= 0 or j >= 0:
            
            while i >= 0:
                if s[i] == '#':
                    
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    
                    skip_s -= 1
                    i -= 1
                else:
                    
                    break
          
           
            while j >= 0:
                if t[j] == '#':
                    
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    
                    skip_t -= 1
                    j -= 1
                else:
                    
                    break
          
           
            if i >= 0 and j >= 0:
                
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                
                return False
          
            
            i -= 1
            j -= 1
      
        
        return True