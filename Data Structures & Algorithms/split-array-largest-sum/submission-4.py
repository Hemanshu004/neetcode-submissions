class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(m):
            curr=0
            count=1
            for num in nums:
                if curr+num>m:
                    curr=num
                    count+=1
                else:
                    curr+=num
            return count<=k

        l=max(nums)
        r=sum(nums)
        res=r
        while l<=r:
            m=(l+r)//2
            if check(m):
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res