class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        res=[]
        for r in range(k-1,len(nums)):
            ele=max(nums[l:r+1])
            res.append(ele)
            l+=1
        return res