class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx=0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                curr=prices[j]-prices[i]
                maxx=max(maxx,curr)
        return maxx
