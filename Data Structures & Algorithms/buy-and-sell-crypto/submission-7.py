class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minBuy=prices[0]
        for sell in prices:
            maxp=max(maxp,sell-minBuy)
            minBuy=min(minBuy,sell)
        return maxp