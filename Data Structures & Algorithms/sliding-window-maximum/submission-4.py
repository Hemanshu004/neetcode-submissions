class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        res=[]
        while l<=len(nums)-(k-1) and r<=len(nums)-1:
            i=max(nums[l:r+1])
            res.append(i)
            l+=1
            r+=1
        return res