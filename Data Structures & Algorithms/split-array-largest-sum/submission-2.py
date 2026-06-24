class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def cansplit(largest):
            subarray=0
            cursum=0
            for n in nums:
                cursum +=n
                if cursum>largest:
                    subarray +=1
                    cursum=n
            return subarray+1<=k

        l,r=max(nums),sum(nums)
        while l<=r:
            m=(l+r)//2
            if cansplit(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
