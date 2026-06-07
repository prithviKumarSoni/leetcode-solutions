"""
Problem: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Pattern: Hashing + Sorting
Key Idea:
- Anagrams have the same characters in sorted order
- Use the sorted string as a hash key
- Group all strings with the same sorted key together
Time: O(n * k log k)
Space: O(n * k)

where:
n = number of strings
k = average length of each string
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            sorted_key = "".join(sorted(string))
            hashmap[sorted_key].append(string)
        return list(hashmap.values())
