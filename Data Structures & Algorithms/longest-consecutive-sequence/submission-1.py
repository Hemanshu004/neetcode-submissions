class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak=0
        store=set(nums)
        for num in nums:
            curr,streak=num,0
            while curr+streak in store:
                streak +=1
            
            max_streak=max(max_streak,streak)
        return max_streak