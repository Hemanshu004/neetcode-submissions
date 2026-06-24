class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        k=len(nums)/2
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        for key,val in dict.items():
            if val>k:
                return key

