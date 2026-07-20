class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = prices[0]
        maxprofit = 0
        for price in prices:
            profit = price - minval
            minval = min(minval,price)
            maxprofit = max(maxprofit,profit)
        
        return maxprofit
