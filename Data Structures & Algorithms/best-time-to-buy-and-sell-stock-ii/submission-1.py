class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price=0
        for i in range(len(prices)-1):
            j=i+1
            if prices[i]<prices[j]:
                price+=prices[j]-prices[i]
            
        return price