class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=0
        l=0
        r=1
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                max_p=max(max_p,profit) 
            else:
                l=r
            r+=1
        return max_p