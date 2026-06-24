class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total=0
        l=0
        length=float("inf")
        for r in range(len(nums)):
            total+=nums[r]
            while  total>=target:
                total-=nums[l]
                length=min(length,r-l+1)
                l+=1
        return length if length!=float("inf") else 0


    