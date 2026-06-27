class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def checksplit(m):
            split=1
            total=0
            for num in nums:
                if total+num>m:
                    split+=1
                    total=num
                else:
                    total+=num
            return split<=k

        l=max(nums)
        r=sum(nums)
        while l<=r:
            m=(l+r)//2
            if checksplit(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res