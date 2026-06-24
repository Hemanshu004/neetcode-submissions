class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res=r
        def canship(cap):
            curr=cap
            ships=1
            for w in weights:
                if curr<w:
                    ships+=1
                    curr=cap
                curr-=w
            return ships<=days

        while l<=r:
            cap=(l+r)//2
            if canship(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res