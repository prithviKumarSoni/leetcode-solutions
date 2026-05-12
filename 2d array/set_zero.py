"""
Problem: Set Matrix Zeroes
Link: https://leetcode.com/problems/set-matrix-zeroes/
Pattern: Matrix Traversal + Row/Column Marking
Key Idea:
- Track rows and columns containing 0 using separate arrays
- First pass: mark affected rows and columns
- Second pass: set matrix cells to 0 based on markers
Time: O(m * n)
Space: O(m + n)
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        rowtrack = [0 for _ in range(r)]
        coltrack = [0 for _ in range(c)]

        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1

        for i in range(0,r):
            for j in range(0,c):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0