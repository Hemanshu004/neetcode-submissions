class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=cur=0
        min_array=float("inf")
        for r in range(len(nums)):
            cur+=nums[r]
            while cur>=target:
                min_array=min(min_array,r-l+1)
                cur -=nums[l]
                l+=1
        return 0 if min_array==float("inf") else min_array