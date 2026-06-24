class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('inf')
        l=0
        sun=0
        for r in range(len(nums)):
            sun +=nums[r]

            while sun>=target:
                res=min(res,r-l+1)
                sun -=nums[l]
                l+=1
        return 0 if res==float('inf') else res