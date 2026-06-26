class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(cap):
            cur=cap
            ships=1
            for w in weights:
                if cur<w:
                    cur=cap
                    ships+=1
                cur-=w
            return ships<=days

        
        l=max(weights)
        r=sum(weights)
        res=float("inf")
        while l<=r:
            m=(l+r)//2
            if canship(m):
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res