class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res=r
        def canship(cap):
            currcap=cap
            ships=1
            for w in weights:
                if currcap-w<0:
                    ships+=1
                    currcap=cap
                currcap-=w
            return ships<=days

        while l<=r:
            cap=(l+r)//2
            if canship(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res