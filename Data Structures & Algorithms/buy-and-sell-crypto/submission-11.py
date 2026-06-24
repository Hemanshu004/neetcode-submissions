class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        r=1
        l=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxp=max(maxp,profit)
            else:
                l=r
            r+=1
        return maxp