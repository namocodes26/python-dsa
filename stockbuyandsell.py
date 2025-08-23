from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        n = len(prices)
        profit = 0
        for i in range(n-1):
            if prices[i+1]>prices[i]:
                profit += prices[i+1]-prices[i]
            
        return profit
            