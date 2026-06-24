class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        for a in range(len(nums)):
            if a>0 and nums[a]==nums[a-1]:
                continue
            
            for b in range(len(nums)-1,a+2,-1):
                if b<len(nums)-1 and nums[b]==nums[b+1]:
                    continue

                c=a+1
                d=b-1
                while c<d:
                    sun=nums[a]+nums[b]+nums[c]+nums[d]
                    if sun<target:
                        c+=1
                    elif sun>target:
                        d-=1
                    elif sun==target:
                        res.append([nums[a],nums[b],nums[c],nums[d]])
                        c+=1
                        d-=1
                        while c<d and nums[c]==nums[c-1]:
                            c+=1
                        while c<d and nums[d]==nums[d+1]:
                            d-=1    
        return res
                            

