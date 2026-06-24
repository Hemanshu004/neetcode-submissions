class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        m=(l+r)//2
        return nums[m]