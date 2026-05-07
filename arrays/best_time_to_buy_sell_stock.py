"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Pattern: Greedy / Sliding Minimum
Key Idea:
- Track the minimum price seen so far
- Calculate profit for each day using current price - minimum price
- Update maximum profit whenever a larger profit is found
Time: O(n)
Space: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit