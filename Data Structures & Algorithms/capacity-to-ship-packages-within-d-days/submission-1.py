class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        while l<=r:
            k=(l+r)//2
            curr=0
            ships=1
            for w in weights:
                if curr+w>k:
                    curr=0
                    ships+=1
                curr+=w
            if ships<=days:
                res=k
                r=k-1
            else:
                l=k+1
            
        return res