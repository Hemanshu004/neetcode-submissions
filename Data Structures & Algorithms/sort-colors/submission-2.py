class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=0
        for j in range(len(nums)):
            if nums[j]==0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp      
                i+=1
        for j in range(len(nums)):
            if nums[j]==1:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp      
                i+=1     
        return nums     