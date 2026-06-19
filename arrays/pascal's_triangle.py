"""
Problem: Pascal's Triangle
Pattern: Simulation / Array Construction
Key Idea: Build each row using the previous row. First and last elements are 1, middle elements are sums of adjacent elements from the previous row.
Time: O(n²)
Space: O(n²)
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for row_index in range(numRows - 1):
            current_row = [1]
            previous_row = triangle[-1]

            for j in range(len(previous_row) -1):
                current_row.append(previous_row[j] + previous_row[j+1])

            current_row.append(1)

            triangle.append(current_row)

        return triangle
            