class Solution:
    def trap(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        left,right=h[l],h[r]
        res=0       
        while l<r:
            if left<right:
                l+=1
                left=max(left,h[l])
                res +=left-h[l]
                
            else:
                r-=1
                right=max(right,h[r])
                res+=right-h[r]
        return res
