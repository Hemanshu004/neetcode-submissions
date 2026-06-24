class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i ,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                three=a+nums[j]+nums[k]
                if three<0:
                    j+=1
                elif three>0:
                    k-=1
                else:
                    res.append([a,nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return res

            
