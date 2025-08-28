class Solution:
    def maximumProfit(self, prices):
        n = len(prices)
        profit = 0
        max_profit = 0
        
        min_price = prices[0]
        for i in range(0,n-1):
            if min_price > prices[i+1]:
                min_price = prices[i+1]
            else:
                profit = prices[i+1]- min_price
                max_profit = max(profit,max_profit)
            
 
        return max_profit