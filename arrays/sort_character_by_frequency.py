"""
Problem: Sort Characters By Frequency
Pattern: Hashing + Sorting
Key Idea: Count the frequency of each character, then sort the characters by frequency in descending order and build the result string.
Time: O(n log k)
Space: O(k)
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        return "".join(
            ch * count
            for ch, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)
        )