class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        length=len(nums)/2
        for i in range(len(nums)):
            dict[nums[i]]=dict.get(nums[i],0)+1
        
        for i,num in dict.items():
            if num>length:
                return i
    